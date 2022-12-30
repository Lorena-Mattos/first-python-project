# Exercício para calcular IMC

nome   = input('Qual é seu nome? ').capitalize()
idade  = input('Qual é sua idade? ')
altura = float(input('Qual é a sua altura? '))
peso   = float(input('Quanto você pesa? '))

imc = peso / altura ** 2

result = f'{nome} tem {altura:.2f} de altura, sua idade é {idade} anos e pesa {peso:.2f} Kg. Seu IMC é: {imc:.2f}'
print(result)

magreza   = 18.5
normal    = 19
sobrepeso = 29
obesidade = 30 

if imc < magreza:
    print(f"{nome} cuidado, seu IMC indica magreza")
    
elif imc >= normal:
    print(f"{nome} seu IMC está normal")

elif imc >= sobrepeso:
    print(f"{nome} seu IMC indica sobrepeso")

elif imc > obesidade:
    print(f"{nome} cuidado, seu IMC indica obesidade")

else:
    print('Não há indicações de IMC')