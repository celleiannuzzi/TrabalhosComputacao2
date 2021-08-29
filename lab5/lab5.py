""" Laboratório 5, Computação 2 - Marcelle Iannuzzi - DRE 118056472 """

# Exercício 1 - Função absoluto

def absoluto(numero):
    """ Essa função tem o objetivo de retornar o valor absoluto de um número, e caso o valor
    de input seja diferente do esperado, ele gera um print notificando o erro."""
    try:
        return abs(float(numero)) #retorna o valor absoluto de um número
    except TypeError:
        #faz o tratamento de erro caso receba um Tipo diferente do esperado, como lista, tupla etc
        print("Erro, a função espera um valor do tipo inteiro ou flutuante.") 
    except ValueError:
        #faz o tratamento de erro caso receba diretamente um valor diferente do esperado, como strings
        print("Erro, a função espera um valor numérico, e não string.")

#Exercício 2 - classe Loja e seus métodos

class Loja:

    #Letra a
    def __init__(self, nome, produtos = {}):
        """ Cria um objeto da classe Loja, recebendo o nome e seus produtos """
        self.nome = nome
        self.produtos = produtos

    #Letra b
    def adicionarProduto(self, categoria, marca):
        """ Adiciona marcas a uma determinada categoria de produtos """
        try:
            self.produtos[categoria].add(marca) # tenta adicionar a nova marca a sua categoria
        except KeyError:
            # se a categoria não existir, retornando KeyError, ela é criada e seu conjunto de
            # marcas atualizado
            self.produtos.update({categoria: {marca}})

    #Letra c
    def verCategoria(self, categoria):
        """ Retorna todas marcas da categoria dada como input. Se a categoria não existir é
         alertado com uma mensagem."""
        try:
            return self.produtos[categoria]
        except KeyError:
            # se a categoria não existir, retornando KeyError, é mostrado uma mensagem
            return print("Categoria {} não catalogada\n".format(categoria))

    #Letra d
    def removerMarca(self, marca):
        """ Remove uma determinada marca de todos os conjuntos de produtos que ela esteja """
        for keys in self.produtos: # para cada chave no dicionário
            self.produtos[keys].discard(marca) #remove a marca do conjunto
            
    # Letra d - método alternativo
    def removerMarca2(self, marca):
        """ Remove uma determinada marca de todos os conjuntos de produtos que ela esteja,
        e caso ela não seja encontrada, é alertado por uma mensagem.
        
        ---------------------- // ----------------------
        
        O método .discard() não da erro caso o item não exista no conjunto, diferente do
        método .remove(), e como no cabeçalho da questão 2-d não pedia tratamento de erros
        nesse método específico da classe, achei melhor deixar um método alternativo com o
        .remove() e tratamento de erros como função 'removerMarca2', que irá ter o mesmo
        efeito do .discard() porém através do try/except. """
        for keys in self.produtos:
            try:
                self.produtos[keys].remove(marca)
            except KeyError:
                continue




        
        
        
    



