from datahandler import generateData
from results import Alt, AltExtra

def start():
    result,myDados,time1,time2,golsTime2,golsTime1,numeroJogos = Alt()
    print(numeroJogos," JOGOS SIMULADOS!")
    for x in range(len(result)):
        print("\n",result[x],"% Das simulações resultaram em: ",myDados.columns.values[0]," ",golsTime1[x]," X ",golsTime2[x]," ",myDados.columns.values[1])
    if golsTime1[0] == golsTime2[0]:
        print("TEMOS UM EMPATE, TEMPO EXTRA")
        result,myDados,time1,time2,golsTime2,golsTime1,numeroJogos = AltExtra(golsTime1[0],golsTime2[0])
        print(numeroJogos," JOGOS EXTRAS SIMULADOS!")
        for x in range(len(result)):
            print("\n",result[x],"% Das simulações resultaram em: ",myDados.columns.values[0]," ",golsTime1[x]," X ",golsTime2[x]," ",myDados.columns.values[1])

def getSelecoes():
    i = True
    j = True
    selecao1 = [] 
    selecao2 = []
    while(i is True):
        selecao1 = inputSelecao()
        selecao2 = inputSelecao()
        print("O jogo será entre: " + str(selecao1['Seleção']) + "X" + str(selecao2["Seleção"]))
        print("Sendo:")
        print(str(selecao1))
        print(str(selecao2))
        print("Você confirma que os dados passados estão corretos? (S/N)")
        while(j is True):
            resp = input()
            if (resp == "S") or (resp == "s"):
                 j = False
                 i = j
                 break
            elif (resp == "N") or (resp == "n"):
                j = False
                break
            else:
                print("Digite apenas S ou N")
                
        print(str(selecao1["Seleção"]))
        if not selecao1["Goleiro"]:
            selecao1 = {'Seleção':"Brasil",'Goleiro':[397],'Ataque':[299],'MeioCampo':[2,114,54,488,295],'Defesa':[89,63,140,124]}

        if not selecao2["Goleiro"]:
            selecao2 = {'Seleção':"Belgica",'Goleiro':[12],'Ataque':[7,50,374],'MeioCampo':[11,274,183],'Defesa':[90,86,806,56]}
    
    return (selecao1, selecao2)


def inputSelecao():
    print("Digite o nome da seleção:")
    nome = input()
    print("Agora, através do arquivo XLSX digite o id do goleiro da seleção:")
    goleiro = input()
    print("Digite o id dos jogadores em posição de ataque separando-os por vírgulas:")
    ataque = input()
    print("Digite o id dos jogadores em posição de meio campo separando-os por vírgulas:")
    meioCampo = input()
    print("Digite o id dos jogadores em posição de defesa separando-os por vírgulas:")
    defesa = input()

    return {'Seleção':str(nome),'Goleiro':goleiro,'Ataque':ataque,'MeioCampo':meioCampo,'Defesa':defesa}


print("Bem vindo ao simulador de jogos da Copa do mundo 2018!")
print("Preencha os dados das seleções para a simulação, caso os dados\nestejam zerados a seleção a ser utilizada será Brasil x Bélgica")
selecao1, selecao2 = getSelecoes()
generateData(selecao1, selecao2)
start()
