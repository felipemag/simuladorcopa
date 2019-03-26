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
Através dos dados obtidos no Kaggle, é utilizado o a teoria dos jogos de forma simplificada para simular ações de cada jogador realizada durante o jogo, usando os seguintes parâmetros gerados a partir do time criado:

- Meio (MEIO):
Capacidade do time no meio campo partir para o ataque.

- Ataque (ATK):
Habilidade do time de atacar, seja a defesa ou o goleiro do adverário.

- Defesa (DF):
Habilidade do time de poder se defender do ataque do adversário, evitando a bola partir para o goleiro.

- Habilidade do goleiro (GK):
Habilidade do goleiro de sobressair ao ataque do adversário.

Para utilizá-lo basta executar o seguinte comando:

```
py main.py 
```

Depois você precisa preencher adequadamente os dados de acordo com o arquivo CompleteDataset.xlsx, caso nada seja preenchido será utilizado o valor padrão dos times Brasil x Belgica.

Você pode personalizar algumas configurações do simulador através do arquivo simulatorConfig.json.


## Referências:

- Descrição do algorítimo: http://www.iaees.org/publications/journals/selforganizology/articles/2014-1(3-4)/a-new-game-theory-algorithm-simulates-soccer-matches.pdf
- Dados: https://www.kaggle.com/thec03u5/fifa-18-demo-player-dataset/version/2