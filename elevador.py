# Desenvolva um sistema capaz de coletar, processar e apresentar informações obtidas a partir de uma pesquisa. A pesquisa tem 
# como objetivo entender o perfil dos moradores de um prédio, para isso, será necessário coletar respostas para as seguintes perguntas: 
# Qual elevador que utilizava com mais frequência;
# (Elevador A, Elevador B, Elevador C)
# Qual período em que utilizava o elevador:
# (M=Matutino,   V=Vespertino,   N=Noturno)
# Construa um algoritmo que faça a leitura, calcule e mostre:
# Qual o elevador mais utilizado e em que período se concentra o maior fluxo
# ****Qual o período mais utilizado de todos;
# Qual a diferença porcentual entre o mais usado dos horários e o menos usado;

def analiseElev (lista):
    cont = {}  
    contA = contB = contC = maxElev = 0
    contM = contV = contN = maxPeriod = 0

    for i in range (len(lista)):
        dupla = tuple(lista[i])
        print(dupla,'DUPLA')

        if dupla in cont:
            cont[dupla] += 1

        else:
            cont[dupla] = 1

    for x, y in cont:

        if x == 'A':
            contA += 1
        elif x == 'B':
            contB += 1
        elif x == 'C':
            contC += 1
        
        if y == 'M':
            contM += 1
        elif y == 'V':
            contV += 1
        elif y == 'N':
            contN += 1

    if contM > contV and contM > contN:
        maxPeriod = contM
    if contV > contM and contV > contN:
        maxPeriod = contV
    if contN > contV and contN > contM:
        maxPeriod = contN

    if contA > contB and contA > contC:
        maxElev = contA
    elif contB > contA and contB > contC:
        maxElev = contB
    elif contC > contB and contC > contA:
        maxElev = contC

    print(maxPeriod)
    
    difPeriod = maxPeriod / (contM + contV + contN)


    print (cont)
    print(cont.values(),' Total lista')



    maiorElev = 0
    
    

list_elevador = []

while True:

    elevador = input('Qual o elevador que você usa com mais frequência? (A/B/C)').upper()
    periodo = input('Qual o périodo que você mais usa o elevador? (M/V/N)').upper()

    if elevador in ['A', 'B', 'C'] and periodo in ['M', 'V', 'N']:
        list_elevador.append([elevador, periodo])
    
    else:
        print('Resposta incorreta, por favor preencha novamente!')

    sair = input('Deseja continuar respondendo?(S/N)').upper()
    if sair == 'N':
        break

    print(list_elevador)

analiseElev(list_elevador)


    









