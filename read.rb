#!/usr/bin/ruby

file = File.open("sudoku.out", "r")
data = file.read
file.close

size = 3
size_2 = size * size

data = data[4,data.length].split

cleaned = Array.new
data.each do |s|
  if (!s.start_with?( "-") and s!="0" and s.length==3)
  cleaned.push s
  end
end

sudoku = Array.new(size_2+1) {Array.new(size_2+1)}
  
cleaned.each do |s|
  sudoku[s[0].to_i][s[1].to_i]=s[2].to_i
end

output = ""
for row in 1 .. size_2
  for column in 1 .. size_2
    output << "#{sudoku[row][column]} "
  end
  output <<  "\n"
end

puts output
