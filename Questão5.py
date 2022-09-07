#Aluna Livia Menezes
#Escreva uma classe “Quadrado”, crie dois métodos que retornem a
#área do quadrado e o perímetro, não crie a instância nesse exercício

lado = int(input("Informe a medida do lado do quadrado\n"))

class Quadrado:
    
    
    def area(self,lado):
        area = lado**2
        return f"A área do quadrado é: {area}"

    def perimetro(self,lado):
        perimetro=lado*4
        return f"O perímetro do quadrado é: {perimetro}"

resultado = Quadrado()

print(resultado.area(lado))
print(resultado.perimetro(lado))