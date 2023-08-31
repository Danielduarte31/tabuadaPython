#**************************************************
# OBJETIVO: CALCULAR UMA SEQUENCIA DE UMA TABUADA
# DATA:31/08/2023
# AUTOR: DANIEL DUARTE
# VERSÃO: 1.0
#*************************************************
#ENTRADA DE DADOS
tabuada = float(input('Digite um número para a tabuada:'))
numeroMax = int(input('Até qual número você deseja que a tabuada vá?'))
contador = 0
#PROCESSAMENTO DE DADOS
while(contador <= numeroMax):
    resultado = tabuada * contador
    print(tabuada ,'x',contador,'=',resultado)
    contador = contador + 1