# Exercício para calcular IMC

nome = input('Qual é seu nome? ').capitalize()

idade = input('Qual é sua idade? ')

altura = input('Qual é a sua altura? ')
float_altura = float(altura)

peso = input('Quanto você pesa? ')
int_peso = int(peso)

imc = int_peso / float_altura ** 2


result = f'{nome} tem {float_altura:.2f} de altura, sua idade é {idade} anos e pesa {int_peso} Kg. Seu IMC é: {imc}'
print(result)

magreza = 18.5
normal = 19
sobrepeso = 29
obesidade = 30 

if imc < magreza:
    print(nome, 'cuidado, seu IMC indica magreza')
    
elif imc >= normal:
    print(nome, 'seu IMC está normal')

elif imc >= sobrepeso:
    print(nome, 'seu IMC indica sobrepeso')

elif imc > obesidade:
    print(nome, 'cuidado, seu IMC indica obesidade')

else: