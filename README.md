# 📖 Local PDF Flipbook

Um visualizador de flipbooks interativo, moderno e totalmente **local**, construído com **HTML5**, **JavaScript**, **PDF.js** e a biblioteca **PageFlip**. Transforme qualquer arquivo PDF em um livro virtual elegante com efeito de virada de páginas realista, executando tudo diretamente no seu navegador.

## 📸 Prévia do Projeto

![Demonstração do Flipbook Local](screenshot.png)

## 🚀 Funcionalidades

* **100% Local e Privado:** Roda inteiramente na sua máquina, sem envio de dados para servidores externos ou dependência de serviços pagos.

* **Seletor de Arquivos Dinâmico:** Escolha e carregue qualquer arquivo PDF do seu computador instantaneamente através de uma interface intuitiva.

* **Renderização de Alta Qualidade:** Utiliza o *PDF.js* da Mozilla para extrair e desenhar cada página do documento com precisão em canvas de alta resolução.

* **Efeito de Virada de Página Realista:** Baseado na biblioteca *PageFlip*, oferecendo sombras dinâmicas, suporte a capas e navegação fluida.

* **Leve e Sem Instalação Complexa:** Não requer frameworks pesados (como React ou Vue); basta um navegador moderno e opcionalmente um servidor HTTP local simples.

## 🛠️ Tecnologias Utilizadas

* [**PDF.js**](https://mozilla.github.io/pdf.js/)**:** Para leitura e renderização de arquivos PDF no lado do cliente.

* [**PageFlip**](https://nodus.com.ua/en/page-flip/)**:** Para criar o efeito físico e interativo de folhear páginas.

* **HTML5 / CSS3 / JavaScript (ES6+):** Código limpo, modular e estruturado em um único arquivo de fácil manutenção.

## ⚙️ Como Executar o Projeto

Como os navegadores modernos aplicam restrições de segurança (CORS) para leitura direta de arquivos locais via JavaScript, é recomendável rodar o projeto através de um servidor HTTP local leve (como o nativo do Python).

### Passo 1: Preparar os arquivos

1. Crie uma pasta para o seu projeto (ex: `meu-flipbook`).

2. Salve o código principal com o nome de `index.html` dentro dessa pasta.

3. Salve a imagem de visualização do projeto com o nome de `screenshot.png` na mesma pasta.

### Passo 2: Iniciar um servidor local

Abra o seu terminal (Prompt de Comando, PowerShell ou Terminal do VS Code) na pasta do projeto e execute um dos comandos abaixo de acordo com sua preferência:

* **Com Python (Recomendado):**

  ```bash
  python -m http.server 8000
  ```

  *(Se utilizar Python 3, o comando acima funciona na grande maioria dos sistemas).*

* **Com Node.js (Alternativa):**

  ```bash
  npx http-server
  ```

### Passo 3: Acessar no Navegador

Abra o seu navegador de preferência (Chrome, Firefox, Edge, etc.) e acesse o endereço gerado pelo servidor:
👉 **`http://localhost:8000`**

## 📖 Como Usar

1. Ao abrir a página inicial, você verá um painel de seleção com a opção de escolher um arquivo PDF.

2. Clique no botão de seleção de arquivos e escolha qualquer PDF armazenado no seu computador.

3. Aguarde alguns segundos enquanto o sistema processa e renderiza as páginas do documento.

4. O flipbook será aberto automaticamente! Arraste as bordas das páginas ou clique nas extremidades para folhear o seu documento.

## 📂 Estrutura do Projeto

```text
meu-flipbook/
│
├── index.html       # Arquivo único contendo toda a estrutura, estilos e lógica JS
└── screenshot.png   # Imagem de demonstração do projeto
```

## 💡 Dicas de Customização

Se desejar alterar o tamanho visual do flipbook, localize o trecho correspondente no código JavaScript do arquivo `index.html` e ajuste os parâmetros de largura e altura (`width` e `height`):

```javascript
const flipBook = new St.PageFlip(bookContainer, {
    width: 500,  // Largura de cada página
    height: 700, // Altura de cada página
    showCover: true,
    maxShadowOpacity: 0.5
});
```

## 📜 Licença

Este projeto é de código aberto e está sob a licença MIT. Sinta-se à vontade para modificar, estilizar e adaptar para os seus próprios projetos e portfólios!