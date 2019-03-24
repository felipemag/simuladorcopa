# Simulador Copa 2018

## Instalação

É requirido os seguintes pacotes para usar esse script:

- pandas
- openpyxl
- xlsxwriter


Para instalar ultilize o seguinte comando: 

```
py -m pip install -r requirements.txt
```

## Descrição

Este é um simples simulador de jogos criado durante a copa do mundo de 2018, os dados utilizados são do jogo FIFA 2018.
Para utilizá-lo basta executar o seguinte comando:

```
py main.py 
```

Depois você precisa preencher adequadamente os dados de acordo com o arquivo CompleteDataset.xlsx, caso nada seja preenchido
será utilizado o valor padrão dos times Brasil x Belgica

Você pode personalizar algumas configurações do simulador através do arquivo simulatorConfig.json


## Referências:

- Descrição do algorítimo: http://www.iaees.org/publications/journals/selforganizology/articles/2014-1(3-4)/a-new-game-theory-algorithm-simulates-soccer-matches.pdf
- Dados: https://www.kaggle.com/thec03u5/fifa-18-demo-player-dataset/version/2