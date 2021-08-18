""" Laboratório 1, Computação 2 - Marcelle Iannuzzi

Exercício 1 - Função concatena """

def concatena(str1, str2, m, n):
    return str1[int(m):] + str2[:-int(n)]
""" retorna a primeira string sem os m primeiros caracteres e a segunda sem os n últimos

Exercício 2 - Sublista """

def sublista(numreais, m, n):
    novalista = [x for x in numreais if (x > m) and (x < n)]
    return novalista
""" filtra e retorna uma lista com os números maiores que m e menores que n

Exercício 3 - Função fun """

def fun(palavra, listapalavras):
    stringretorno = palavra # inicia a string que será retornada com o primeiro valor
    contador = 0 #inicia contador
    for x in listapalavras: # para cada string na lista de strings
        stringretorno += " "+listapalavras[contador] # adiciona um espaço e uma string da lista
        contador += 1 # aumenta o contador para ir para a próxima string da lista
    return stringretorno # retorna a frase formada pela string palavra + strings da lista
""" junta a string (palavra), passada como argumento, em uma frase com as strings de uma lista
(listapalavras) separadas por uma espaço

Exercício 4 letra (a) - Função de euler """

import math #importa a biblioteca de funções matemáticas do python

def numeroEuler(n):
    numeuler = 0 # inicia o numero como 0
    for x in range(0,n): #para cada número de 0 ao limite passado como argumento n
        numeuler += 1 / (math.factorial(x)) #faz o somatório do número antigo com o próximo
        # sendo 1 sobre o fatorial do número atual x
    return numeuler #retorna o número de euler calculado até o limite n
""" retorna o número de euler calulado até um limite (n) passado por argumento

Exercício 4 letra (b) -  Função de precisão de euler """

def precisaoEuler(erro):
    contador = 0 # inicia contador
    numeuler = math.e # salva o número de euler
    numeulerCalculado = numeroEuler(contador) # salva o número de euler calculado pela função
    # iniciando em 0 
    erroabsoluto = math.fabs(numeuler - numeulerCalculado)
#salva a diferença entre o número de euler retornado pelo python e o número de euler
#calculado pela função
    while erroabsoluto > erro:
#fica em loop até o erro absoluto ser menor do que o erro passado como parâmetro
        contador += 1 # aumenta o contador a cada loop (pois ele já começou em 0)
        numeulerCalculado = numeroEuler(contador)
#salva o número calculado novamente, com contador aumentado
        erroabsoluto = math.fabs(numeuler - numeulerCalculado) #faz a diferença novamente
    return contador
""" retorna o contador com o número de vezes que precisa ser calculado o número de euler
para a diferença entre o erro absoluto ser menor que o erro passado como parâmetro

Exercício 4 letra (c) - Função main """

def main():
    erroTolerado = float(input("Qual o erro máx tolerado?\n ")) #pega o input do usuário
    termosCalculadosEuler = precisaoEuler(erroTolerado) #chama a função que faz o cálculo
    print(termosCalculadosEuler) # printa o valor retornado
    return()

if __name__ == "__main__": 
    main() # chama a main


    
        



