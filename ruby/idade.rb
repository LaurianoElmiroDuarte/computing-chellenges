resultado = ''

loop do
    puts resultado
    puts 'Selecione uma das seguintes opções'
    puts '1 - Descubrir a idade de uma pessoa'
    puts '0 - Sair'
    print 'Opção: '

    option = gets.chomp.to_i
    if option == 1
        print 'Digite aqui seu ano de nascimento: '
        data_de_nascimento = gets.chomp.to_i
        print 'Digite o ano atual: '
        ano_atual = gets.chomp.to_i
        idade = ano_atual - data_de_nascimento
        resultado = "Quem nasceu no ano de #{data_de_nascimento}, tem #{idade} anos em #{ano_atual}"
    elsif option == 0
        break
    else 
        resultado = 'Opção invalida'
    end 
    system = 'clean'
end