# Descubra quais os tipos de cursos dos alunos de Joinville

Neste desafio, você deverá inferir quais os tipos de cursos que os alunos de Joinville estão cursando. Por exemplo: são cursos de educação? De ciências, matemática e computação? De engenharia? Descubra através deste desafio. 

## Tópicos

Neste desafio você aprenderá:

- Machine learning
- Classificação

## Requisitos

Você precisará de python 3.6 (ou superior) e do gerenciador de pacotes pip **apenas para submeter o desafio. Você pode solucionar o mesmo em qualquer linguagem.**

O recomendado é você utilizar um [ambiente virtual](https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais). Para isto, execute os comandos como no exemplo abaixo:

    pip3 install virtualenv
    virtualenv venv -p python3
    source venv/bin/activate 
    pip install -r requirements.txt

Ao terminar o desafio, você pode sair do ambiente criado com o comando `deactivate`

## Detalhes

Neste desafio você usará os dados no arquivo `train.csv` para criar um modelo que será utilizado para inferir os tipos de cursos dos alunos de Joinville (coluna `NO_OCDE_AREA_GERAL`) no arquivo `test.csv`. Para tal, você deve criar um arquivo `answer.csv` com colunas `index` e `NO_OCDE_AREA_GERAL`, onde os valores da coluna `index` são as do arquivo `test.csv` e as da `NO_OCDE_AREA_GERAL` são a saída do seu modelo.
