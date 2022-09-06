#Aluna: Lívia Menezes

#Questão 1:
#Dada as seguintes informações: Pessoa, cpf, nome e idade, crie uma
#classe onde teremos o retorno do documento, o retorno do nome e
#verificação de tipo de pessoa, onde um método irá receber como
#parâmetro “F” ou “N” para trazer fumante ou não fumante.
#Feito isso, crie uma instância e retorne esses valores.

class Questao1:

    def __init__(self):
        self.nome = ""
        self.cpf = ""
        self.idade = ""
        self.pessoa = ""
        self.fumante = ""

        self.pessoa = input("Informe o tipo de pessoa [Fisica/Juridica]:\n")
        self.nome = input("Digite o nome:\n")
        self.idade = input("Informe a idade:\n")
        if self.pessoa == "Fisica" or self.pessoa == "fisica":
            self.cpf = input("Digite o CPF:\n")

    def fumante(self):
        fum = True

        self.fumante = input("Favor informar se o indivíduo é fumante ou não. Digite F para fumante e N para não-fumante\n")
        while fum:
            if self.fumante != "F" and self.fumante != "N" and self.fumante != "n" and self.fumante != "f":
                self.fumante = input("Informação inválida. Favor informar se o indivíduo é fumante ou não. Digite F para fumante e N para não-fumante")
            else:
                fum = False
        
        if self.fumante == "f" or self.fumante =="F":
            return f"Segue abaixo dados do usuário\
            \nNome: {self.nome}\
            \nIdade {self.idade}\
            \nTipo de Pessoa: {self.pessoa}\
            \n{self.nome} é fumante"

        else:
            return f"Segue abaixo dados do usuário\
            \nNome: {self.nome}\
            \nIdade {self.idade}\
            \nTipo de Pessoa: {self.pessoa}\
            \n{self.nome} é fumante"

