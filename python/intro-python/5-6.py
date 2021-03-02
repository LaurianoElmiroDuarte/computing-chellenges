# Altere o programa anterior para exibir os resultados no mesmo formato de uma tabela.

n = int(input('Tabuada de ? '))
x = 0

while x <= 9:
    print(f'{n}x{x} = {n * x}')
    x = x + 1
