#!/usr/bin/env python3

# Modifique o programa anterior para imprimir de 1 até o número digitado pelo usuário,
# mas, dessa vez, apensar os numeros ímpares.

fim = int(input('Digite o último número da sequência: '))

x = 0

while x <= fim:
    if x % 2 != 0:
        print(x)
    x = x + 1


