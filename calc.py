import os

print("Calculadora teste\n")

print("Digite o primeiro numero: ")
num1 = int(input())
print("Digite o segundo numero: ")
num2 = int(input())
print("Digite a operação que será realizada(+, -, *, /): ")
operacao = input()

resultado = 0

if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    resultado = num1 / num2
else:
    os.system("cls")
    print("Operação inválida\n")

print("Resultado:", resultado)