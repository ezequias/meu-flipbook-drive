# 📖 Google Drive PDF Flipbook

Um visualizador de flipbooks interativo e moderno que permite carregar e folhear arquivos PDF diretamente de links públicos do **Google Drive**, utilizando **HTML5**, **JavaScript**, **PDF.js** e a biblioteca **PageFlip**.

## 📸 Prévia do Projeto

![Demonstração do Flipbook do Google Drive](screenshot.png)

## 🚀 Funcionalidades

* **Integração com o Google Drive:** Abra qualquer PDF armazenado na sua nuvem apenas colando o link de compartilhamento público.
* **Proxy Python Inteligente:** Um servidor local em Python que contorna as restrições de CORS do navegador e trata automaticamente avisos de confirmação de segurança (arquivos grandes) do Google Drive.
* **Renderização de Alta Qualidade:** Utiliza o *PDF.js* da Mozilla para desenhar cada página em canvas de alta resolução.
* **Efeito de Virada de Página Realista:** Baseado na biblioteca *PageFlip*, oferecendo sombras dinâmicas, suporte a capas e navegação fluida.
* **Leve e Sem Complicação:** Não requer bancos de dados ou instalações complexas na nuvem.

## 🛠️ Tecnologias Utilizadas

* [**PDF.js**](https://mozilla.github.io/pdf.js/) — Leitura e renderização dos arquivos PDF no navegador.
* [**PageFlip**](https://nodus.com.ua/en/page-flip/) — Efeito físico e interativo de folhear páginas.
* **Python (http.server / urllib):** Servidor HTTP local e proxy para download seguro dos arquivos do Drive.
* **HTML5 / CSS3 / JavaScript (ES6+)**

## ⚙️ Como Executar o Projeto

### Passo 1: Preparar os arquivos
Certifique-se de que a sua pasta de projeto contém os seguintes arquivos:
* `index.html` (interface web e lógica de renderização)
* `server.py` (servidor Python e proxy para o Google Drive)
* `screenshot.png` (imagem de demonstração do projeto)

### Passo 2: Iniciar o servidor local
Abra o seu terminal (PowerShell ou Prompt de Comando) na pasta do projeto e execute:

```bash
python server.py

Passo 3: Acessar no Navegador
Abra o seu navegador e acesse:
👉 http://localhost:8000

📖 Como Usar
No seu Google Drive, clique com o botão direito no PDF desejado, selecione Compartilhar e configure o acesso como "Qualquer pessoa com o link" (Leitor). Copie o link.

Abra http://localhost:8000 no navegador.

Cole o link de compartilhamento do Google Drive na caixa de texto.

Clique em Gerar Flipbook e aguarde o processamento. O livro virtual abrirá na tela pronto para ser folheado!

📂 Estrutura do Projeto
Plaintext
meu-flipbook-drive/
│
├── index.html       # Interface web do flipbook e leitor PDF.js
├── server.py        # Servidor Python com proxy universal para o Drive
└── screenshot.png   # Imagem de demonstração


📜 Licença
Este projeto é de código aberto sob a licença MIT.