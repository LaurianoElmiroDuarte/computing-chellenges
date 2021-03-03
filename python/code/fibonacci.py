def fib(x):    #escreve a série Fibonacci até x
    a, b = 0, 1
    while a < x:  # valor não ultrapassa x
        print(a, end=' ')
        a, b = b, a + b
    print()

