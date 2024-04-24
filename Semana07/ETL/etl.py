import yfinance as yf
import json

# Defina os pares das moedas no formato correto para forex
symbols = ["USDBRL=X"]

# Defina o período de busca (1 ano)
start_date = "2014-04-16"
end_date = "2024-04-10"

# Crie um dicionário vazio para armazenar os dados
data = {}

# Para cada símbolo, extraia os dados e adicione ao dicionário
for symbol in symbols:
    # Baixe os dados históricos
    historical_data = yf.download(symbol, start=start_date, end=end_date)
    
    # Verifique se os dados foram baixados com sucesso
    if not historical_data.empty:
        # Converta as chaves do DataFrame de Timestamp para string
        historical_data.index = historical_data.index.strftime('%Y-%m-%d')
        # Converta o DataFrame em um dicionário
        symbol_data = historical_data.to_dict()

        # Adicione os dados ao dicionário principal
        data[symbol] = symbol_data

# Salve o dicionário em um arquivo JSON
with open("cotacoes.json", "w") as outfile:
    json.dump(data, outfile, indent=4)
