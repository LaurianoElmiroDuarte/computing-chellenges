#!/usr/bin/env python3

# Escreva um programa que leia dois numeros. Imprima a divisão inteira do primeiro pelo segundo, assim como o resto da divisão. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender o quociente da divisão de dois números como a quantidade de vezes que podemos retirar o divisor do dividendo. Logo, 20 / 4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20.


x = int(input("Digite o primeiro numero: "))

y = int(input("Digite o segundo numero: "))

r = 0

q = 0

n = y

while n <= x:
    r = x - n
    if r < y:
        print(f'O resto é: {r}')
        
    q = q + 1 
    if n == x:
        print(f'O quociente é: {q}')
        
    n = n + y  
