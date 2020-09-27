print "Digite um número qualquer: "
numero = gets.chomp.to_i

print "Digite um outro numero qualquer: "
numerox = gets.chomp.to_i

adicao = numero + numerox

puts "A soma dos dois números é: #{adicao}"


print "Meu nome é: "
nome = gets.chomp
print "Minha idade é: "
idade = gets.chomp

puts "Meu nome é #{nome} e minha idade é #{idade}"

print "Primeiro numero é: "
primeiro = gets.chomp.to_i
print "Segundo numero é: "
segundo = gets.chomp.to_i

adicao = primeiro + segundo
subtracao = primeiro - segundo
multiplicacao = primeiro * segundo
divisao = primeiro / segundo

puts "A soma é: #{adicao} substracao é: #{subtracao}, mutiplicação é:#{multiplicacao} e a divisão:#{divisao}"