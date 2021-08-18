""" Lista 3 - Computação 2 - Marcelle Iannuzzi """

class VeiculoAutomotor(): # superclasse
    # classe que classifica um veículo
    def __init__(self, dono, placa, combustivel): # método construtor da classe 
        self.dono = dono
        self.placa = placa
        self.combustivel = combustivel
    
    def __str__(self): # método de retorno de string da superclasse
        return "Dono: {}, placa: {}, combustível: {}".format(self.dono, self.placa, self.combustivel)

""" Exercício 1 - letra (a) """

class Automovel(VeiculoAutomotor): #subclasse que herda a superclasse VeiculoAutomotor
    # e tem mais alguns atributos únicos
    def __init__(self, dono, placa, combustivel, lugares, portas, ano): # método contrutor da subclasse
        super().__init__(dono, placa, combustivel) # recebendo dados da superclasse
        self.lugares = lugares
        self.portas = portas
        self.ano = ano

# Exercício 1 - letra (b)
    def __str__(self): # método de retorno de string da subclasse
        return super().__str__() + ", lugares: {}, portas: {}, ano: {}".format(self.lugares, self.portas, self.ano)

# Exercício 1 - letra (c)
    def trocarDono (self, novoDono): # método para trocar o nome do dono do automóvel
        if novoDono == self.dono: # verifica se o dono já é o atual
            print("O dono atual já é {}".format(self.dono))
        else:
            self.dono = novoDono # troca o nome do dono do automóvel

""" Exercício 2 - letra (a) """

class Caminhao(VeiculoAutomotor): # subclasse que herda a superclasse VeiculoAutomotor
    # e tem mais um atributo referente ao peso
    def __init__(self, dono, placa, combustivel, cargaMax): # método contrutor da subclasse
        super().__init__(dono, placa, combustivel) # recebendo dados da superclasse
        self.cargaMax = cargaMax

    def __str__(self): # método de retorno de string da subclasse
        return super().__str__() + ", carga máxima: {} toneladas".format(self.cargaMax)
        
        
