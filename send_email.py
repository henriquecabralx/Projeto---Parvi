import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv


def send_email(resumo):
    # Carrega variáveis do .env
    load_dotenv()

    email = os.getenv('EMAIL')
    senha = os.getenv('PASSWORD')

    if not email or not senha:
        print("❌ Erro: EMAIL ou PASSWORD não encontrados no arquivo .env")
        return

    destinatarios = [
        'paulo.andre@parvi.com.br',
        'thiago.jose@parvi.com.br'
    ]

    # Monta o e-mail
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = ", ".join(destinatarios)
    msg['Subject'] = "Relatório de Citações - Desafio RPA Python"

    # Corpo do e-mail
    msg.attach(MIMEText(resumo, 'plain'))

    # Anexa o CSV
    filename = 'quotes.csv'
    if not os.path.exists(filename):
        print("❌ Arquivo 'quotes.csv' não encontrado. Execute primeiro o scraping.")
        return

    with open(filename, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            'Content-Disposition',
            f'attachment; filename={filename}',
        )
        msg.attach(part)

    # Envia o e-mail
    try:
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(email, senha)
        servidor.sendmail(email, destinatarios, msg.as_string())
        servidor.quit()
        print("✅ E-mail enviado com sucesso!")

    except Exception as e:
        print(f"❌ Falha ao enviar o e-mail: {e}")


# Executa quando roda diretamente
if __name__ == "__main__":
    from data_processing import process_data

    resumo = process_data()
    if resumo:
        send_email(resumo)
