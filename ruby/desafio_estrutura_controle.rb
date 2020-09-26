resultado_total = ''

loop do
    puts resultado_total
    puts 'Selecione uma das seguintes opções'
    puts '1 - Somar'
    puts '2 - Subtrair'
    puts '3 - dividir'
    puts '4 - multiplicar'
    puts '0 - sair'
    print 'Opção: '
    
    option = gets.chomp.to_i
    if option == 1
        print 'Digite aqui o primeiro numero: '
        x = gets.chomp.to_i
        print 'Digite aqui o segundo numero: '
        y = gets.chomp.to_i
        re = x + y
        resultado_total = "O valor da adição é: #{re}"
    elsif option == 2
        print 'Digite aqui o primeiro numero: '
        x = gets.chomp.to_i
        print 'Digite aqui o segundo numero: '
        y = gets.chomp.to_i
        re = x - y
        resultado_total = "O valor da subtração é: #{re}"
    elsif option == 3
        print 'Digite aqui o primeiro numero: '
        x = gets.chomp.to_i
        print 'Digite aqui o segundo numero: '
        y = gets.chomp.to_i
        re option = x / y
        resultado_total = "O valor da divisão é: #{re}"
    elsif option == 4
        print 'Digite aqui o primeiro numero: '
        x = gets.chomp.to_i
        print 'Digite aqui o segundo numero: '
        y = gets.chomp.to_i
        re = x * y
        resultado_total = "O valor da multiplicação é: #{re}"
    elsif option == 0
        break
    else
        break
    end
    system = 'clean'
end