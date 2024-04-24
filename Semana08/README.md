# Aula 08

Olá! Ao iniciar um projeto em Python, é fundamental aderir a um conjunto de boas práticas para garantir clareza, eficiência e facilidade de uso. Essas práticas incluem:

- A inclusão de um arquivo README.md no projeto, que deve conter uma introdução ao projeto, uma descrição detalhada do que foi desenvolvido e instruções passo a passo para configurar o ambiente necessário para rodar o projeto.

- A criação de um arquivo chamado requirements.txt, que lista todas as bibliotecas externas e suas respectivas versões utilizadas no projeto. Esse arquivo deve garantir que qualquer pessoa ou sistema que tente executar o projeto possa instalar as dependências necessárias.

## Acesso ao Colab

O conteúdo da aula também pode ser acessado pelo link **usando uma conta do Google**: https://drive.google.com/file/d/1sySax7x2uVg9Kdv5zgQqGEuRtHhOGCZO/view?usp=sharing

**Atenção:** Escolha a opção **Copiar para o Drive** para começar os estudos.

## Configuração do Ambiente

### Instalando Dependências (**Windows**)

Crie uma pasta chamada BigData, clique com o botão do lado direito e selecione a opção abrir no terminal. 

No terminal cole os comandos abaixo para a criação, ativação do ambiente virtual e instalação das dependências.

```bash
python -m venv venv && .\venv\Scripts\activate && pip install -r requirements.txt
``` 


<details>
  <summary>Instalando Dependências (Linux/Mac)</summary>
  
    Criação e ativação do ambiente virtual
    
            python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
    
</details>


**BONS ESTUDOS!**