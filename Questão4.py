#Aluna Lívia Menezes
#Crie um professor de classe com atributos nome, idade e salário, onde
#o salário deve ter um método privado que não pode ser acessado fora da classe.
#a. Crie um método para acessar o método privado, onde é passada
#a identificação do usuário se ele pode ou não acessar.

class Professor:
    def __init__(self,nome,idade,salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario

    def infosgerais(self):
        return f"O(a) Prof se chama {self.nome} e tem {self.idade} anos\n"

    def limsalario(self):
        return "Acesso negado"

    def exporsalario(self):
        nome = input("Quem pergunta?\n")
        cargo = input("Qual cargo?\n")
        if cargo == "CEO" and nome == "Bill Gates":
            return f"O(a) Prof {self.nome} ganha R$ {self.salario}"
        else:
            return f"{self.limsalario()}"


nome = input("Digite o nome do Professor:\n")
idade = input("Qual a idade?\n")
salario = input(f"Qual salário do Prof {nome}?\n")

professor = Professor(nome,idade,salario)

print(professor.infosgerais())

print(professor.exporsalario())