#!/usr/bin/ruby

file = File.open("sudoku.out", "r")
data = file.read
file.close

size = 9

data = data[4,data.length].split

cleaned = Array.new
data.each do |s|
  if (!s.start_with?( "-") and s!="0" and s.length==3)
  cleaned.push s
  end
end

sudoku = Array.new(size+1) {Array.new(size+1)}
  
cleaned.each do |s|
  sudoku[s[0].to_i][s[1].to_i]=s[2].to_i
end

output = ""
for row in 1 .. size
  for column in 1 .. size
    output << "#{sudoku[row][column]} "
  end
  output <<  "\n"
end

puts output
