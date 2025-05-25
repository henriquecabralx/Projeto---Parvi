from scraping import scrape_quotes
from data_processing import process_data
from send_email import send_email


if __name__ == "__main__":
    scrape_quotes()
    resumo = process_data()
    if resumo:
        send_email(resumo)
