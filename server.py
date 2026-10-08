import http.server
import json
import urllib.request
import urllib.parse
import os
import re

PORT = 8000

# Defina aqui o caminho da sua pasta local sincronizada com o Google Drive (Google Drive para Desktop), se desejar
DRIVE_FOLDER_PATH = r"C:/Users/Ezequias/Google Drive" # Ajuste se necessário

class DualFlipbookHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        
        # 1. Rota para listar os PDFs da pasta local sincronizada
        if parsed_path.path == '/api/list-pdfs':
            self.send_response(200)
            self.send_header('Content-type', 'application/json; charset=utf-8')
            self.end_headers()
            
            target_folder = DRIVE_FOLDER_PATH if os.path.exists(DRIVE_FOLDER_PATH) else os.getcwd()
            pdf_files = []
            
            try:
                for file in os.listdir(target_folder):
                    if file.lower().endswith('.pdf'):
                        pdf_files.append({
                            "name": file,
                            "path": os.path.join(target_folder, file)
                        })
                self.wfile.write(json.dumps(pdf_files).encode('utf-8'))
            except Exception as e:
                self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))
            return

        # 2. Rota para servir o PDF da pasta local
        elif parsed_path.path == '/api/serve-local-pdf':
            query_params = urllib.parse.parse_qs(parsed_path.query)
            file_path = query_params.get('path', [None])[0]
            
            if not file_path or not os.path.exists(file_path):
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b"Arquivo nao encontrado.")
                return

            try:
                with open(file_path, 'rb') as f:
                    pdf_data = f.read()
                self.send_response(200)
                self.send_header('Content-type', 'application/pdf')
                self.end_headers()
                self.wfile.write(pdf_data)
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(str(e).encode('utf-8'))
            return

        # 3. Rota Proxy para baixar o PDF via Link Público do Google Drive (Tratando vírus/tamanho e redirecionamentos)
        elif parsed_path.path == '/api/proxy-drive':
            query_params = urllib.parse.parse_qs(parsed_path.query)
            url_or_id = query_params.get('url', [None])[0]
            
            if not url_or_id:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"URL nao fornecida.")
                return

            # Extrai o ID do arquivo do link do Google Drive
            file_id = url_or_id
            match = re.search(r'/d/([a-zA-Z0-9-_]+)', url_or_id)
            if match:
                file_id = match.group(1)
            else:
                match_id = re.search(r'id=([a-zA-Z0-9-_]+)', url_or_id)
                if match_id:
                    file_id = match_id.group(1)

            download_url = f"https://drive.google.com/uc?export=download&id={file_id}"

            try:
                req = urllib.request.Request(
                    download_url, 
                    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
                )
                
                with urllib.request.urlopen(req) as response:
                    pdf_data = response.read()
                    
                    # Trata páginas de confirmação de segurança/vírus para arquivos grandes
                    if b'uc-download-link' in pdf_data or b'confirm=' in pdf_data:
                        match_confirm = re.search(r'confirm=([0-9A-Za-z_]+)', pdf_data.decode('utf-8', errors='ignore'))
                        if match_confirm:
                            confirm_token = match_confirm.group(1)
                            download_url_confirmed = f"{download_url}&confirm={confirm_token}"
                            req_conf = urllib.request.Request(
                                download_url_confirmed, 
                                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
                            )
                            with urllib.request.urlopen(req_conf) as resp_conf:
                                pdf_data = resp_conf.read()

                    self.send_response(200)
                    self.send_header('Content-type', 'application/pdf')
                    self.end_headers()
                    self.wfile.write(pdf_data)
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(f"Erro ao baixar do Google Drive: {str(e)}".encode('utf-8'))
            return

        return super().do_GET()

if __name__ == '__main__':
    print(f"Servidor rodando em http://localhost:{PORT}")
    http.server.test(HandlerClass=DualFlipbookHandler, port=PORT)