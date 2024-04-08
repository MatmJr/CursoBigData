import requests
import sqlite3

def create_university_db(country):
    # URL da API
    url = f"http://universities.hipolabs.com/search?country={country}"
    
    # Fazer a requisição à API
    response = requests.get(url)
    universities = response.json()

    # Criar ou conectar ao banco de dados SQLite
    conn = sqlite3.connect('universities.db')
    c = conn.cursor()
    
    # Criar a tabela, se não existir
    c.execute('''
        CREATE TABLE IF NOT EXISTS universities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            country TEXT,
            state_province TEXT,
            web_pages TEXT,
            domains TEXT
        );
    ''')

    # Inserir dados no banco de dados
    for university in universities:
        c.execute('''
            INSERT INTO universities (name, country, state_province, web_pages, domains)
            VALUES (?, ?, ?, ?, ?);
        ''', (
            university['name'],
            university['country'],
            university['state-province'],
            ', '.join(university['web_pages']),  # Convertendo listas em strings
            ', '.join(university['domains'])
        ))
    
    # Commitar as mudanças e fechar a conexão
    conn.commit()
    conn.close()

