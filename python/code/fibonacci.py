def fib(x):    #escreve a série Fibonacci até n 
    a, b = 0, 1
    while a < x:
        print(a, end=' ')
        a, b = b, a + b
    print()
    
