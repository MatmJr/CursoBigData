# Aula 01

Olá! Ao iniciar um projeto em Python, é fundamental aderir a um conjunto de boas práticas para garantir clareza, eficiência e facilidade de uso. Essas práticas incluem:

- A inclusão de um arquivo README.md no projeto, que deve conter uma introdução ao projeto, uma descrição detalhada do que foi desenvolvido e instruções passo a passo para configurar o ambiente necessário para rodar o projeto.

- A criação de um arquivo chamado requirements.txt, que lista todas as bibliotecas externas e suas respectivas versões utilizadas no projeto. Esse arquivo deve garantir que qualquer pessoa ou sistema que tente executar o projeto possa instalar as dependências necessárias.

## Atividade 01

1 - Crie uma pasta chamada BigData.

2 - Abra a pasta no VS Code e comece a configurar o seu ambiente de trabalho.

Windows

    2.1 - Dentro da pasta, clique com o botão do lado direito do mouse , escolha a opção abrir no terminal e digite code . 
    2.2 - Abra o terminal no VS Code e crie um ambiente virtual python chamado venv
     Terminal: python -m venv venv
    2.3 - Ativar o ambiente virtual
     Terminal: .\venv\Scripts\activate

<details>
  <summary>Linux/Mac:</summary>
  
    2.1 - Dentro da pasta, clique com o botão do lado direito do mouse , escolha a opção abrir no terminal e digite code . 
    2.2 - Abra o terminal no VS Code e crie um ambiente virtual python chamado venv
     Terminal: python3 -m venv venv
    2.3 - Ativar o ambiente virtual
     Terminal: souce venv/bin/activate    
  
</details>

<details>
  <summary>Anaconda:</summary>
  
    2.1 - Dentro da pasta, clique com o botão do lado direito do mouse , escolha a opção abrir no terminal e digite code . 
    2.2 - Abra o terminal no VS Code e crie um ambiente virtual python chamado venv
     Terminal: conda create --name venv
    2.3 - Ativar o ambiente virtual
     Terminal: conda activate ./venv  
  
</details>

&nbsp;

3 - Crie um arquivo chamado README.md dentro da pasta BigData.
     Terminal: echo. > README.md

4 - Crie um arquivo chamado .gitignore dentro da pasta BigData.

    4.1 - Terminal: echo. > .gitignore
    4.2 - Digite na primeira linha do arquivo arquivo venv/
        Terminal: echo venv/ > .gitignore

5 - Crie um aquivo chamado requiremets.txt dentro da pasta BigData.
     Terminal: echo. > requirements.txt


## Atividade 02

1 - Crie um arquivo chamado aula01.ipynb

2 - Instale o pandas no ambiente virtual:
    
    2.1 Terminal: pip install pandas

3 - Adicione pandas ao arquivo requeriments.txt

4 - Abra o arquivo aula01.ipynb

    4.1 Ative o ambiente virtual
     Select Kernel > Python Environment > venv

5 - Importando a primeira base de dados

    5.1 Importe o pandas como pd
    5.2 Crie a variável url = "https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv"
    5.3 Carregue o conjunto de dados da url com o método read_csv do pandas em uma variável chamada data.

**BONS ESTUDOS!**