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

        self.pessoa = input("Informe o tipo de pessoa [Fisica/Juridica]:\n")
        self.nome = input("Digite o nome:\n")
        self.idade = input("Informe a idade:\n")
        if self.pessoa == "Fisica" or self.pessoa == "fisica":
            self.cpf = input("Digite o CPF:\n")

    def fumante(self):
        fum = True

        fumante = input("Favor informar se o indivíduo é fumante ou não. Digite F para fumante e N para não-fumante\n")
        while fum:
            if fumante != "F" and fumante != "N" and fumante != "n" and fumante != "f":
                fumante = input("Informação inválida. Favor informar se o indivíduo é fumante ou não. Digite F para fumante e N para não-fumante")
            else:
                fum = False
        
        if fumante == "f" or fumante =="F":
            return f"Segue abaixo dados do usuário\nNome: {self.nome}\nIdade {self.idade}\nTipo de Pessoa: {self.pessoa}\n{self.nome} é fumante"
        else:
            return f"Segue abaixo dados do usuário\nNome: {self.nome}\nIdade {self.idade}\nTipo de Pessoa: {self.pessoa}\n{self.nome} não é fumante"

    def pf(self):
        return self.pessoa

resolucaoquestao1 = Questao1()
print(resolucaoquestao1.fumante())

#Questão 2:
#Escreva uma classe “PessoaFisica” e herde Pessoa, crie um método
#exclusivo para a classe e acesse-o

class PessoaFisica:
    def __init__(self, pessoa):
        self.pessoa = pessoa

        return self.pessoa

PessoaFisica(resolucaoquestao1.pf())