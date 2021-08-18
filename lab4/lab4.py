""" Lista de exercícios 4 - Marcelle de Macedo Iannuzzi Barbosa - DRE 118056472 """

# Exercício 1 - função contatos

def contatos(contatos:list)->dict:
    """ Esta função recebe uma lista de dicionários, nos quais podem ter chaves iguais em dicionários diferentes. A função
    junta os dicionários fazendo com que os valores dos mesmos se tornem uma listas de valores, para quando houver chaves iguais na junção dos
    dicionários, a chave continuar a mesma e os valores não serem perdidos e sim unidos.

    Entrada: uma lista de dicionários - List(of dict)
    Saída: um dicionário que une os dicionários da lista de entrada - Dict """
    dicNovosContatos = {}
    for dicionario in contatos:
        for valor in dicionario.keys():
            if valor in dicNovosContatos:
                dicNovosContatos[valor].append(dicionario[valor])
            else:
                dicNovosContatos[valor] = [dicionario[valor]]
    return dicNovosContatos
                
# Exercício 2 - Função piano 

def piano(notas:str) -> list:
    """ Esta função recebe um string com os valores de uma nota musical e sua posição no piano, e retorna a
    frequência dessas notas nas diferentes partes de um piano.
    
    Entrada: string com duplas de nota+posição como C1, C2B3 etc - String
    Saída: lista de floats com os valores da frequência de cada nota - List(of float) """
    
    dicFrequencias = {"C": 262, "D": 294, "E": 330, "F": 349, "G": 392, "A": 440, "B": 494} # cria o dicionário com as chaves sendo as notas e os 
    #valores de frequência
    dicValorNotas = {1: -2, 2: -1, 3: 0, 4: 1, 5: 2} #cria um dicionário para saber a qual número o 2 na conta tem que ser elevado
    notasTotais = len(notas)//2 #divide o total de letras da string de entrada por 2 para saber quantos pares de nota+posição tem
    count1 = 0 #inicia dois contadores para pegar a dupla de nota+posição de acordo com o índice delas na string de entrada
    count2 = 2
    listaFrequencias = [] #cria uma lista vazia para receber os valores calculados das frequências
    for x in range(0, notasTotais): #faz um loop de acordo com o número de duplas nota+posição da string de entrada
        notaAtual = notas[count1:count2] #pega a nota+posição que será feita a conta de acordo com o índice na string de entrada com ajuda dos contadores
        listaFrequencias.append(dicFrequencias[notaAtual[0]]*(pow(2, dicValorNotas[int(notaAtual[1])])))
        #adiciona a lista o número de frequência calculado, pegando os valores do dicionário de acordo com a 'notaAtual', cujo primeiro indice (0) é
        #a letra e o índice (1) é o número da parte do piano
        count1+=2 #aumenta os contadores em 2 para seguir para a próxima dupla de nota+posição
        count2+=2
    return listaFrequencias #retorna a lista com os valores de frequência

#Exercício 3 - função rezistor

def rezistor (cor1:str, cor2:str, cor3:str) -> int:
    """ Esta função recebe 3 strings como entrada, sendo as 3 nomes e cores de acordo com a tabela de um resistor. De acordo com as 3 strings
    é feito uma conta para descobrir o valor da resistência, sendo a mesma feita da forma: R = ((Valor da primeira cor)*10+(Valor da
    segunda cor))*(10**(Valor da terceira cor)).

    Entrada: 3 strings, sendo o nome das cores - String
    Saída: int, valor da resistência - Int """
    
    dicValores = {"preto": 0, "marrom": 1, "vermelho": 2, "laranja": 3, "amarelo": 4} #cria o dicionário com os valores das cores
    valor = ((dicValores[cor1]*10+dicValores[cor2]))*pow(10, dicValores[cor3]) #faz a conta para descobrir a resistência
    return valor #retorna o valor da resistência

