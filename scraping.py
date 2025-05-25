from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import csv
import time


def scrape_quotes():
    # Configurações do Chrome
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Opcional: sem abrir janela
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Inicializa o driver automaticamente
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    # Acessa a primeira página
    url = "https://quotes.toscrape.com/js-delayed/"
    driver.get(url)

    all_data = []

    while True:
        # Espera as citações carregarem
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "quote"))
        )

        quotes = driver.find_elements(By.CLASS_NAME, "quote")

        for quote in quotes:
            text = quote.find_element(By.CLASS_NAME, 'text').text
            author = quote.find_element(By.CLASS_NAME, 'author').text
            tags = quote.find_element(By.CLASS_NAME, 'tags').text.replace('\n', ', ')
            all_data.append([text, author, tags])

        # Verifica se tem botão Next
        try:
            next_button = driver.find_element(By.CSS_SELECTOR, 'li.next > a')
            next_button.click()
            time.sleep(1)  # Pequeno delay para não sobrecarregar
        except:
            # Não encontrou botão Next → última página
            break

    driver.quit()

    # Salva no CSV
    with open('quotes.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Citação', 'Autor', 'Tags'])
        writer.writerows(all_data)

    print("✅ Arquivo 'quotes.csv' criado com sucesso com TODAS as páginas!")


if __name__ == "__main__":
    scrape_quotes()
