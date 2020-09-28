#Missão 1
#recebe os valores
puts 'Digite aqui o primeiro numero: '
um = gets.chomp.to_i
puts 'Digite aqui o segundo numero: '
dois = gets.chomp.to_i
puts 'Digite aqui o terceiro numero: '
tres = gets.chomp.to_i
#armazena esses valores no array 
numeros = [um, dois, tres]
#realizar a operação de 'each'
numeros.each do |b|
    puts b ** 2
end

#Missão 2

chave = {}

puts 'Digite a primeira chave'
puts 'Digite o primeiro valor'
chave[um_ = gets.chomp.to_i] = gets.chomp.to_i

puts 'Digite a segunda chave'
puts 'Digite o segundo valor'
chave[dois_ = gets.chomp.to_i] = gets.chomp.to_i

puts 'Digite a terceira chave'
puts 'Digite o terceiro valor'
chave[tres_ = gets.chomp.to_i] = gets.chomp.to_i

chave.each do |key, value|
    puts "Uma das chaves é #{key} e o seu valor é #{value}"    
end

#Missão 3;

Numbers = {a: 10, b: 302, c: 20, d: 25, e: 15}

selection Numbers.select do |key, value|
    key > 