# Aula 02

## Configuração do Ambiente

### Instalando Dependências (Linux)

Criação e ativação do ambiente virtual
```bash
python3 -m venv venv && source venv/bin/activate
``` 
Instalação das libs
```bash
pip install -r requirements.txt
``` 

### Instalando Dependências (Windows)

Criação e ativação do ambiente virtual
```bash
python -m venv venv && .\venv\Scripts\activate
``` 
Instalação das libs
```bash
pip install -r requirements.txt
``` 

**Observação:** Criei um Script para configutação automática no Windows. Seguir os seguintes passos:

- Baixar os arquivos setup.ps1 e requirements.txt na pasta que você criou para a aula.

- Abrir o VSCode na pasta.

- Executar o Command Prompt:

    ```bash
        .\setup.sh
    ```

## Dataset da Aula

O dataset da aula de hoje será retirado do link:

```url
https://drive.google.com/uc?id=1aosoxH9p2Jg3YwqtzQdC6UtWStSEc92G
```


O conjunto de dados original:

```url
https://www.kaggle.com/datasets/ealtman2019/ibm-transactions-for-anti-money-laundering-aml
```