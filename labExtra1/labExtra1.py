""" Lista Extra - Computação 2 - Marcelle de Macedo Iannuzzi Barbosa - DRE 118056472 """

#Exercício 1

class Dinheiro:
    def __init__(self, valor, moeda):
        """ Cria um objeto da classe Dinheiro em uma das seguintes moedas: BRL,
        USD, EUR, JPY, com os atributos de valor e nome da moeda"""
        self.valor = valor
        self.moeda = moeda
        self.Valores = {"USD": 4.012, "EUR": 4.451, "JPY": 0.035} # dicionário que guarda os valores de conversão
        # das outras moedas para BRL
        if moeda != "BRL": # verifica se a moeda criada é BRL ou não
            self.valorReal = valor * self.Valores[moeda] # se não for, guarda o valor em Reais, fazendo a conversão
        else:
            self.valorReal = valor # se a moeda criada já for BRL, então o valor em reais é o próprio valor passado

    def valor_em(self, moeda):
        """Método que retorna o valor do dinheiro de acordo com a moeda passada como parâmetro"""
        if self.moeda == moeda: #verifica se já é a mesma moeda
            return self.valor
        elif moeda == "BRL": # verifica se quer converter para BRL
            return self.valorReal
        else: # caso seja para outra moeda sem ser BRL ou a mesma, faz a conversão
            return self.valorReal/self.Valores[moeda]

    def __str__(self):
        """ Método que retorna uma string com o valor do dinheiro em real """
        return "{} BRL".format(self.valorReal)

#Exercício 2

def BrexitEmployment(sim, nao, trabalha, desempregado):
    """ Função que retorna uma string dizendo qual percentual de pessoas da amostra que votaram sim ou
    não tem trabalho e qual percentual é desempregado """
    totalSN = len(sim.union(nao)) # pega o valor do total de pessoas que votaram sim ou não
    # retorna o percentual pedido
    return "SIM: {:.2f}% trabalham, {:.2f}% estão desempregados".format((len(sim.intersection(trabalha))/totalSN)*100, (len(sim.intersection(desempregado))/totalSN)*100) \
           + "\nNÃO: {:.2f}% trabalham, {:.2f}% estão desempregados".format((len(nao.intersection(trabalha))/totalSN)*100, (len(nao.intersection(desempregado))/totalSN)*100)
    
