#!/usr/bin/env python3

def fib(x):               # escreve a série Fibonacci até 'x'.
    """ Docstrings """    # opcionalmente, pode adicionar uma Docstring.
    a, b = 0, 1           # determina os valores das variaveis 'a' e 'b'.
    while a < x:          # valor não ultrapassa 'x'.
        print(a, end=' ') # printa o valor da variavel 'a'.
        a, b = b, a + b   # as variaveis 'a' e 'b' recebem novos valores.
    print()               # printa uma linha vazia.
f = fib                   # a variavel 'f' recebe a funnção 'fib'

f(2000)
