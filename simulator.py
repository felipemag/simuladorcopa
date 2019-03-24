#from dadosTime import dadosTime
from random import randrange, uniform
import os
import sys
import time
import pandas as pd
import json
from datahandler import openGeneratedData
import datetime  
from kumaraswamy import NumAleatorio


with open('simulatorConfig.json', 'r') as f:
    config = json.load(f)

i = 0
finalizacaoTime1 = 0
finalizacaoTime2 = 0
gol1 = 0
gol2 = 0
posseT2 = 0
posseT1 = 0

tempo = config['tempo']
minuto = config['minuto']
numeroJogos = config['numeroJogos']
maxTempo = config['maxTempo']
maxTempoExtra = config['maxTempoExtra']
ativoComentario = config['ativoComentario']

idTime1 = 0
idTime2 = 1
isGrupo = 0 #grupo = 0 vai ter tempo extra e penalty se empate

def finalizacoes(nome,quantidade):

    global finalizacaoTime1,finalizacaoTime2

    if nome == time1['nome']:
        finalizacaoTime1 = finalizacaoTime1 + 1
    else:
        finalizacaoTime2 = finalizacaoTime2 + 1

def possedeBola(posse):
    global posseT2,posseT1,PorposseT1,PorposseT2
    if posse == 1:
        posseT1 = posseT1 + 1
    elif posse == 0:
        posseT1 = posseT1 + 1
        posseT2 = posseT2 + 1 
    else:
        posseT2 = posseT2 + 1 
    
    PorposseT1 = round(posseT1*100/(posseT1+posseT2))
    PorposseT2 = round(posseT2*100/(posseT1+posseT2))

    return (str(PorposseT1)+" - "+str(PorposseT2)+"")


def Apresentador(comentario,posse):
    global minuto, gol1, gol2, tempo 
    posseTexto = possedeBola(posse)
    
    tempo = tempo + 1
  
    
    time.sleep(minuto) 
    if ativoComentario == 1:
        print(tempo,"\' \t [",gol1," - ",gol2,"] : ",posseTexto," ",comentario)


def startMeioCampo(time1,time2):

    winT1,winT2 = gerarAleatorio(time1['meio'],time2['meio'])
    
    if winT1 == True:
        Apresentador(str(time1['nome'])+" parte para o ataque",0)
        winT1, winT2 = gerarAleatorio(time1['atk'],time2['df'])
        atk_vs_df(winT1,winT2,time1,time2,1)

    elif winT2 == True:
        Apresentador(str(time2['nome'])+" parte para o ataque",0)
        winT1, winT2 = gerarAleatorio(time1['df'],time2['atk'])
        atk_vs_df(winT1,winT2,time1,time2,2)

    return()


def atk_vs_df(winT1,winT2,time1,time2,teamA):

    if teamA == 1:
        if winT1 == False:
            Apresentador(str(time1['nome'])+" perde a bola para a defesa da "+str(time2['nome']),1)
        else:
            atk_vs_goleiro(winT1,winT2,time1,time2)
    else:
        if winT2 == False:
            Apresentador(str(time2['nome'])+" perde a bola para a defesa da "+str(time1['nome']),2)
        else:
            atk_vs_goleiro(winT1,winT2,time1,time2)
    return()
    

def atk_vs_goleiro(winT1,winT2,time1,time2):
    
    if winT1 == True:
        Apresentador(str(time1['nome'])+" passou da defesa",1)
        winT1, winT2 = gerarAleatorio(time1['atk'],time2['gk'])
        if winT1 == True:
            gol(winT1,winT2,time1,time2)
        else:
            Apresentador("Defesa do goleiro do "+str(time2['nome']),1)
            finalizacoes(time1['nome'],1)
    else:
        Apresentador(str(time2['nome'])+" passou da defesa",2)
        winT1, winT2 = gerarAleatorio(time1['gk'],time2['atk'])
        if winT2 == True:
            gol(winT1,winT2,time1,time2)
        else:
            Apresentador("Defesa do goleiro do "+str(time1['nome']),1)
            finalizacoes(time2['nome'],1)
    return()


def gol(winT1,winT2,time1,time2):
    
    if winT1 == True:
        global gol1
        gol1 = gol1 + 1
        Apresentador("Goooool do "+str(time1['nome']),1)
        
    elif winT2 == True:
        global gol2
        gol2 = gol2 + 1
        Apresentador("Goooool do "+str(time2['nome']),2)
        
    return()



            
#Lembrar de Arrumar empate.
def gerarAleatorio(t1,t2):
    
    
    t1 = int(t1*NumAleatorio())
    t2 = int(t2*NumAleatorio())
  
   
    if t1 > t2:
        winT1 = True
        winT2 = False
   
    else:

        winT1 = False 
        winT2 = True
    
    return (winT1,winT2)


def gameStat(gol1,gol2,posseT1,posseT2,time1,time2):
    
    if gol1 > gol2:
        print("Fim de jogo!!!\n",time1['nome']," ganhou a partida por: ",gol1," a ",gol2,"\nObrigado por assistir a está partida!")
    elif gol1 < gol2:
        print("Fim de jogo!!!\n",time2['nome']," ganhou a partida por: ",gol2," a ",gol1,"\nObrigado por assistir a está partida!")
    else:
        print("Fim de jogo!!!\nA partida acabou empatada, esperamos vocês no próximo jogo!")
    return()
    
def startGame(time1,time2, tempoPartida):
    global minuto,i, gol1, gol2, tempo,maxTempo,posseT1,posseT2,finalizacaoTime1,finalizacaoTime2
    i = 0
    gol1 = 0
    gol2 = 0
    posseT2 = 0
    posseT1 = 0
    tempo = 0
    if tempoPartida > maxTempo:
        tempo = maxTempo

    while tempo < tempoPartida:
        startMeioCampo(time1,time2)

    if ativoComentario == 1:
        gameStat(gol1,gol2,posseT1,posseT2,time1,time2)

    resultado=[int(gol1),int(gol2),str(PorposseT1),str(PorposseT2)]
    ChutesGol=[finalizacaoTime1,finalizacaoTime2]
    finalizacaoTime1 = 0
    finalizacaoTime2 = 0
    print(".")
    #resultado=[str(gol1),str(gol2),str(PorposseT1),str(PorposseT2)]

    return(resultado,ChutesGol)

def startGameExtra(time1,time2, tempoPartida, golsTime1,golsTime2):
    global minuto,i, gol1, gol2, tempo,maxTempo,posseT1,posseT2,finalizacaoTime1,finalizacaoTime2
    i = 0
    gol1 = golsTime1
    gol2 = golsTime2
    tempo = maxTempo

    while tempo < tempoPartida:
        startMeioCampo(time1,time2)

    if ativoComentario == 1:
        gameStat(gol1,gol2,posseT1,posseT2,time1,time2)

    resultado=[int(gol1),int(gol2),str(PorposseT1),str(PorposseT2)]
    ChutesGol=[finalizacaoTime1,finalizacaoTime2]
    finalizacaoTime1 = 0
    finalizacaoTime2 = 0
    #resultado=[str(gol1),str(gol2),str(PorposseT1),str(PorposseT2)]

    return(resultado,ChutesGol)

def startSimulador():
    listaResultados = []
    ChutesGolLista = []
    global time1 
    global time2 
    time1,time2 = openGeneratedData()
    
    for x in range(0,numeroJogos):
        #print("Jogo número: ",x)
        resultado,ChutesGol = startGame(time1,time2, maxTempo)
        #print("Resultado jogo: ",x, resultado)
        listaResultados.append(resultado)
        ChutesGolLista.append(ChutesGol)

    df = pd.DataFrame(listaResultados,columns=(time1['nome'],time2['nome'],'Posse1','Posse2'))
    
    now = str(datetime.datetime.now())
   
    now = now.replace(":","-")
    #Exportar resultados para um Excel
    writer = pd.ExcelWriter('HistoricoResultados/Resultados '+now+'.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1')    # Close the Pandas Excel writer and output the Excel file.
    writer.save()

    return (df,listaResultados,numeroJogos,time1['nome'],time2['nome'],ChutesGol)



def tempoExtra(golsTime1,golsTime2):
    print("TEMPO EXTRA")

    if golsTime1 == golsTime2:
        print("Temos um empate na maioria das simulações. Vamos para tempo extra de 30m")
        listaResultados = []
        ChutesGolLista = []
        global time1 
        global time2 
        global numeroJogos

        for x in range(0,numeroJogos):
            resultado,ChutesGol = startGameExtra(time1,time2,maxTempo+maxTempoExtra, golsTime1,golsTime2)
            listaResultados.append(resultado)
            ChutesGolLista.append(ChutesGol)

        df = pd.DataFrame(listaResultados,columns=(time1['nome'],time2['nome'],'Posse1','Posse2'))
        print("----------------------------s")
      
        return (df,listaResultados,numeroJogos,time1['nome'],time2['nome'],ChutesGol)
    return()
