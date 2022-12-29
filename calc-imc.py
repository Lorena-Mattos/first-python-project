# Exercício para calcular IMC

nome = input('Qual é seu nome? ').capitalize()

idade = input('Qual é sua idade? ')

altura = input('Qual é a sua altura? ')
float_altura = float(altura)

peso = input('Quanto você pesa? ')
int_peso = int(peso)

imc = int_peso / float_altura ** 2

result = f'{nome} tem {float_altura:.2f} de altura, sua idade é {idade} anos e pesa {int_peso}Kg. \nSeu IMC é: {imc}'
print(nome, result)

if imc < 18.5:
    print('%s, cuidado, seu IMC indica magreza' % nome)
    
elif imc >= 18.5:
    print('%s, seu IMC está normal' % nome)

elif imc >= 24.9:
    print('%s, seu IMC indica sobrepeso' % nome)

elif imc > 30:
    print('%s, cuidado, seu IMC indica obesidade' % nome)

else:
    print('Não há indicações de IMC')
