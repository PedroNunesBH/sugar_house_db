<h1 align="center">Sugar House Database App</h1>

![MySQL Badge](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Python Badge](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![GIT Badge](https://img.shields.io/badge/git-orange?style=for-the-badge&logo=git&logoColor=white)
![Tkinter Badge](https://img.shields.io/badge/Tkinter-00A68C?style=for-the-badge&logo=python&logoColor=white)



O projeto Sugar House Database App foi desenvolvido para a atividade do Laboratório de Extensão da faculdade Estácio, curso de Análise e Desenvolvimento de Sistemas na disciplina Banco de Dados.

A atividade tem como objetivo desenvolver as habilidades estudadas ao longo do semestre na matéria aplicando-as em um cenário real e de forma conjunta criando envolvimento com a comunidade local através de um projeto social. 

Para o desenvolvimento dessa atividade foi estabelecida uma parceria com uma confeitaria local chamada Sugar House, localizada em Belo Horizonte, Minas Gerais cujo a proprietária é uma microempreendedora individual.

A aplicação consiste no desenvolvimento de um banco de dados em MySQL para facilitar o registro de despesas e encomendas da confeitaria.Para que a proprietária consiga fazer os registros sem o conhecimento técnico de SQL foi criada uma interface gráfica utilizando Python.

## Índice
- [Índice](#índice)
- [Status do Projeto](#status-do-projeto)
- [Layout](#layout)
- [Funcionalidades](#funcionalidades)
- [Variáveis de Ambiente](#variaveis-de-ambiente)
- [Banco de Dados](#banco-de-dados)
- [Como Rodar A Aplicação](#como-rodar-a-aplicação)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Estrutura de Diretórios](#estrutura-de-diretórios)
- [Padrões Utilizados](#padrões-utilizados)
- [Metodologia de Desenvolvimento](#metodologia-de-desenvolvimento)
- [Desenvolvedor](#desenvolvedor)
- [Licença](#licença)

## Status do Projeto
Finalizado ✅


## Layout

**Index**



## Funcionalidades
1. **Visualização dos Registros**: Permite verificar todos os registros das tabelas SQL.
2. **Inserção de Registros**: Inserir novos registros no banco de dados.
3. **Edição de Registros**: Edição dos registros.
4. **Exclusão dos Registros**: Permite excluir registros.

## Variáveis De Ambiente

## Banco de Dados

Para a criação do banco de dados, foi utilizado o **MySQL Workbench** na versão **8.0.34**.

A estrutura do banco de dados inclui as seguintes tabelas:

1. **encomendas**: armazena informações sobre as encomendas realizadas.  
   Para verificar a estrutura da tabela `encomendas`, acesse o diretório `sql` e visualize o arquivo `create_table_encomendas.sql`.

2. **despesas**: armazena informações sobre as despesas.  
   Para verificar a estrutura da tabela `despesas`, acesse o diretório `sql` e visualize o arquivo `create_table_despesas.sql`.
    
## Como Rodar A Aplicação

1. Clone o repositório usando o comando:
    
    git clone https://github.com/PedroNunesBH/sugar_house_db.git

2. Navegue até o diretório do projeto

3. Instale as dependências necessárias listadas no arquivo requirements.txt:

    pip install -r requirements.txt
    
4. Navegue até o diretório 'src'
    
5. Execute o seguinte comando :

    python main.py
    


    

## Tecnologias Utilizadas
- [MySQL](https://www.mysql.com/)
- [Python](https://www.python.org/)
- [Git](https://git-scm.com/)


## Estrutura de Diretórios

    projeto/
    │
    ├── sql/
    │   ├── create_table_encomendas.sql     # Script para criar a tabela de encomendas.
    │   └── create_table_despesas.sql       # Script para criar a tabela de despesas.
    │
    ├── src/
    │   ├── database/
    │   │   ├── display_records.py           # Script para exibir registros do banco de dados.
    │   │   ├── edit_record_window.py        # Script para a interface de edição de registros.
    │   │   ├── insert_expenses.py           # Script para inserir despesas no banco de dados.
    │   │   ├── insert_orders.py             # Script para inserir encomendas no banco de dados.
    │   │   ├── show_db_infos.py             # Script para mostrar informações do banco de dados.
    │   │   └── show_records.py              # Script para mostrar registros armazenados.
    │   │
    │   └── main.py                          # Ponto de entrada principal da aplicação.
    │
    ├── requirements.txt                      # Arquivo com as dependências do projeto.
    └── .gitignore                            # Arquivo que especifica quais arquivos/diretórios o Git deve ignorar.
    
## Padrões Utilizados
1. **Commits Semânticos**: Os commits do projeto seguem o padrão de commits semânticos facilitando o entendimento e a padronização.

## Metodologia de Desenvolvimento


## Desenvolvedor
- [Pedro Henrique Silveira Nunes](https://github.com/PedroNunesBH)

##  Licença
Este projeto está licenciado sob uma licença proprietária. Todos os direitos são reservados ao proprietário do projeto. O uso, modificação ou distribuição deste código não é permitido sem a devida autorização.