hash = {0=> 'zero', 1=> 'um', 2=> 'dois', 3=> 'três', 4=> 'quatro', 5=> 'cinco', 6=> 'seis'}

puts 'Selecionando keys com valores maior que 4'
selection = hash.select do |key, value|
    key > 4
end
puts selection