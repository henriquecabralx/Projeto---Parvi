# 🚀 Desafio de Estágio - RPA com Python

## 📚 Descrição do Projeto
Este projeto tem como objetivo realizar web scraping no site 
[https://quotes.toscrape.com/js-delayed/](https://quotes.toscrape.com/js-delayed/), 
processar os dados coletados e enviar um relatório por e-mail contendo 
um resumo das informações e o arquivo CSV em anexo.

## 🏗 Estrutura do Projeto

rpa_quotes/
├── .env                  # Variáveis sensíveis (NÃO subir para o GitHub)
├── .gitignore            # Arquivos que o Git deve ignorar
├── main.py               # Script principal que executa tudo
├── scraping.py           # Script de scraping (coleta de dados)
├── data_processing.py    # Processamento dos dados do CSV
├── send_email.py         # Envio do e-mail com CSV e resumo
├── requirements.txt      # Dependências do projeto
├── README.md             # Documentação do projeto
└── quotes.csv            # Arquivo CSV gerado (opcional no Git)

## ⚙ Funcionalidades
- ✅ Web scraping de *todas as 10 páginas* do site.
- ✅ Extração de:
  - Citações
  - Autores
  - Tags
- ✅ Salvamento dos dados em um arquivo CSV (quotes.csv).
- ✅ Processamento dos dados:
  - Quantidade total de citações.
  - Autor mais recorrente.
  - Tag mais utilizada.
- ✅ Envio de relatório por e-mail com:
  - ✔ CSV como anexo.
  - ✔ Resumo dos dados no corpo do e-mail.

  ## 🔥 Tecnologias e Bibliotecas Usadas
- Python
- Selenium
- Pandas
- Webdriver-Manager
- smtplib + email (biblioteca nativa para e-mails)
- python-dotenv (para segurança das credenciais)

## 🚀 Como Executar o Projeto

### 🔧 Pré-requisitos
- Python instalado na máquina
- Conta de e-mail com *App Password*
- Git (opcional, recomendado)

### ⿡ Clone o repositório
```bash
git clone https://github.com/seu-usuario/rpa_quotes.git
cd rpa_quotes
```
