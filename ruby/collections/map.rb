arei = [1, 2, 3, 4, 5, 6]

novu_arei = arei.map do |a|
    a * 3.7
end

puts "\n Array Original"
puts "#{arei}"

puts "\n Novo Array"
puts "#{novu_arei}"



arei.map! do |b|
    b * 3.14
end

puts "\n New Array"
puts "#{arei}"