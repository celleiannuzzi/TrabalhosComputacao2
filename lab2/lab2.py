""" lista de exercícios 2 - Computação 2 - Marcelle Iannuzzi 

cada exercício está mapeado nos comentários do código """

class Aluno:
    def __init__(self, nome, DRE, matricula = "ativa"):
        #Cria um objeto da classe Aluno com atributos nome, DRE, matricula
        self.nome = nome
        self.DRE = DRE       
        self.matricula = matricula

    def alterarMatricula(self, matricula):
        #Altera a matricula
        if self.matricula == matricula:
            print("A matrícula já está " + matricula)
        else:
            self.matricula = matricula
            print("A matrícula foi alterada para " + matricula)
            
    def dados(self):
        """Retorna uma descrição de um objeto da classe"""
        return "{}\t{}\tmatricula {}".format(self.nome, str(self.DRE), self.matricula)

    def __str__(self):
        #Retorna uma descrição de um objeto da classe
        return "{} {} matricula {}".format(self.nome, str(self.DRE), self.matricula)

class Disciplina:
    #Classe representa o conceito de uma disciplina na UFRJ
    def __init__(self, nome, vagas = 0):
        #Cria um objeto da classe com atributos nome, vagas, alunos
        self.nome = nome
        self.vagas = vagas
        self.alunos = [] # self.alunos é um atributo global criado automaticamente

    def __add__(self, other):
        #Junta duas disciplinas se o nome delas for idêntico
        if self.nome == other.nome:
            return Disciplina(self.nome, self.vagas + other.vagas)
        else:
            print("Não foi possível juntar as turmas")
    
    def inscreverAluno(self, aluno):
        #Inscreve um objeto da classe Aluno na disciplina se tiver
        #vagas livres ou o Aluno não for ainda inscrito na disciplina
        if len(self.alunos) < self.vagas and aluno not in self.alunos:
            self.alunos.append(aluno)
        elif aluno in self.alunos:
            print("aluno {} já está inscrito na disciplina".format(aluno.nome))
        else:           
            print("Vagas esgotadas")

# Exercício 1 - letra (a) 
    def consultarVagas(self):
    #Retorna uma descrição da situação das vagas
        return "Vaga totais: {}. Vagas livres: {}.".format(self.vagas, (self.vagas - len(self.alunos)))

# Exercício 1 - letra (b) 
    def __str__(self):
        if self.vagas == (self.vagas - len(self.alunos)):
            return self.nome + ", sem alunos inscritos.\n" + Disciplina.consultarVagas(self)
        else:
            alunos = ""
            for x in self.alunos:
                alunos = alunos + str(x) + "\n"
            return self.nome + ", alunos inscritos:\n"+ alunos + Disciplina.consultarVagas(self)

#importando a classe datetime
import datetime

class Pessoa: # classe que representa uma pessoa real

    #Exercício 2 - letra (a)
    def __init__(self, nome, dataNascimento, nomeDeMae, nomeDePai):
        # método construtor da classe pessoa
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.nomeDeMae = nomeDeMae
        self.nomeDePai = nomeDePai
        
    # Exercício 2 - letra (b)
    def idade(self, data = datetime.date.today()): # inicia o método com valor defalt da data de hoje
        # transforma a data do dia do nascimento da Pessoa em tipo datetime a vaiável dataNascimento o
        # com o método da classe datetime, colocando com parâmetro (ano, mês, dia) em formato de inteiro
        dataNascimento = datetime.date(int(self.dataNascimento.split("/")[2]), int(self.dataNascimento.split("/")[1]), int(self.dataNascimento.split("/")[0]))
        # Faz o cálculo de quantos anos a pessoa está, fazendo ano atual - ano de nascimento, e diminui em 1 ou 0
        # de acordo com o resultado da verificação de se o dia e mês de nascimento já passou ou não
        anosvida = data.year - dataNascimento.year - ((data.month, data.day) < (dataNascimento.month, dataNascimento.day))
        return str(anosvida) # retorna os anos de vida em formato de string
    
    # Exercício 2 - letra (c)
    def __str__(self):
        return "nome: " + self.nome + ", idade: " + Pessoa.idade(self) + ", mae: " + self.nomeDeMae + ", pai: " + self.nomeDePai
        
        

    
        
