import pandas as pd


def process_data():
    try:
        # Lê o arquivo CSV
        df = pd.read_csv('quotes.csv')

        # Total de citações
        total_citacoes = len(df)

        # Autor mais recorrente
        autor_mais_recorrente = df['Autor'].value_counts().idxmax()

        # Tag mais utilizada
        tag_mais_usada = (
            df['Tags']
            .str.split(', ')
            .explode()
            .value_counts()
            .idxmax()
        )

        # Monta o resumo
        resumo = (
            f"📊 RESUMO DO RELATÓRIO:\n\n"
            f"→ Total de citações: {total_citacoes}\n"
            f"→ Autor mais recorrente: {autor_mais_recorrente}\n"
            f"→ Tag mais utilizada: {tag_mais_usada}\n"
        )

        print(resumo)

        return resumo

    except FileNotFoundError:
        print("❌ Arquivo 'quotes.csv' não encontrado. Execute primeiro o scraping.")
        return None


# Executa quando roda diretamente
if __name__ == "__main__":
    process_data()
