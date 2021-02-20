class Program(array):
    @staticmethod
    def Main(args):
        Target()
    @staticmethod
    def Target():
        listaTemp = List[int]()
        resultado = List[int]()
        print("Target: ")
        target = Parse(ReadLine())
        nums = List[int]()
        print("Digite o tamanho do array: ")
        total = Parse(ReadLine())
        WriteLine("Digite os números: ")
        i = 0
        while (i < total):
            numero = Parse(ReadLine())
            listaTemp.Add(numero)
            i += 1
        listaTemp.Sort()
        i = 0
        while (i < listaTemp.Count):
            if ((listaTemp[i] + listaTemp[(i + 1)]) == target):
                resultado.Add(i)
                resultado.Add((i + 1))
                print("[{},{}]".format(i, (i + 1)))
                break
            i += 1


print(Target)