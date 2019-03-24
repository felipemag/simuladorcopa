from simulator import startSimulador, tempoExtra
import numpy as np
import time



def Alt():
    numeroDeResultados = 5

    df,listaResultados,numeroJogos,time1,time2,ChutesGol = startSimulador()
    df['Quantidade'] = 1
    df['teste'] = np.where(df[time1]> df[time2], 1,(np.where(df[time1] < df[time2],'VT2',(np.where(df[time1] == df[time2],'EMP','ERROR')))))
    df = df.drop('Posse1',axis=1)
    df = df.drop('Posse2',axis=1)

    myDados = df.groupby([time1,time2]).sum().reset_index()
    myDados = myDados.sort_values(['Quantidade'],ascending=False)

    result = []
    golsTime2 = []
    golsTime1 =[]
   
    for x in range(0,numeroDeResultados):
      
        top =  myDados.iloc[x:x+1]
        
        
        golsTime1.append(int(top[time1]))
        golsTime2.append(int(top[time2]))
        top = int(top['Quantidade']/numeroJogos*100)
        result.append(top)
    
    
    

    return (result,myDados,time1,time2,golsTime2,golsTime1,numeroJogos)

def AltExtra(golsTime1,golsTime2):
    numeroDeResultados = 5
    print("ALT EXTRA")
    
    df,listaResultados,numeroJogos,time1,time2,ChutesGol = tempoExtra(golsTime1,golsTime2)

    df['Quantidade'] = 1

    df['teste'] = np.where(df[time1]> df[time2], 1,(np.where(df[time1] < df[time2],'VT2',(np.where(df[time1] == df[time2],'EMP','ERROR')))))
    
    df = df.drop('Posse1',axis=1)
    df = df.drop('Posse2',axis=1)

    myDados = df.groupby([time1,time2]).sum().reset_index()
   
    myDados = myDados.sort_values(['Quantidade'],ascending=False)

    result = []
    golsTime2 = []
    golsTime1 =[]
   
    for x in range(0,numeroDeResultados):
      
        top =  myDados.iloc[x:x+1]
        
        
        golsTime1.append(int(top[time1]))
        golsTime2.append(int(top[time2]))
        top = int(top['Quantidade']/numeroJogos*100)
        result.append(top)
    
    return (result,myDados,time1,time2,golsTime2,golsTime1,numeroJogos)
