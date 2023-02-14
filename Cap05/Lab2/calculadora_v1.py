# Calculadora em Python

# Author: Sergio Lima
# Created on: Feb, 5th 2023

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

def sum_oper(num1,num2):
    return num1 + num2

def sub_oper(num1,num2):
    return num1 - num2

def mult_oper(num1,num2):
    return num1 * num2

def div_oper(num1,num2):
    return num1 / num2

def get_signal(option):
    signal_array = ["+","-","*","/"]
    return signal_array[option-1]

def calc(num1, num2, signal):
    operations = {'+': sum_oper(num1, num2), '-': sub_oper(num1, num2), 
                  '*': mult_oper(num1, num2), '/': div_oper(num1, num2)}
    return operations[signal]


print("\n******************* Calculadora em Python *******************")

print("\nSelecione o numero da operacao desejada:")

print("\n1 - Soma")
print("2 - Subtracao")
print("3 - Multiplicacao")
print("4 - Divisao")

option=int(input("\nDigite sua opcao (1/2/3/4): "))

num1=int(input("\nDigite o primeiro numero: "))

num2=int(input("\nDigite o segundo numero: "))

signal = get_signal(option)

res = calc(num1, num2, signal)

print("\n")
print(num1,signal,num2,"=",res)
print("\n")


