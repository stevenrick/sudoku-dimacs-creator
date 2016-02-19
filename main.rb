#!/usr/bin/ruby
size = 9
numbers = size

atoms = size * size * numbers
clauses = 0

dimacs = ""



dimacs << "c at least one number in each entry\n"
for i in 1 .. size
  for j in 1 .. size
    for k in 1 .. numbers
      dimacs << "#{i}#{j}#{k} "
    end
    dimacs << "0 \n"
    clauses += 1
  end
end

dimacs << "c each number at most once in each row\n"
for i in 1 .. size
  for j in 1 .. size
    for k in 1 .. numbers
      for j_s in j+1 .. numbers
        dimacs << "-#{i}#{j}#{k} -#{i}#{j_s}#{k} 0 \n"
        clauses += 1
      end
    end
  end
end

dimacs << "c each number at most once in each column\n"
for i in 1 .. size
  for j in 1 .. size
    for k in 1 .. numbers
      for i_s in i+1 .. numbers
        dimacs << "-#{i}#{j}#{k} -#{i_s}#{j}#{k} 0 \n"
        clauses += 1
      end
    end
  end
end

dimacs << "c each number at most once in each block\n"
for k in 1 .. numbers
  for m in 0 .. 2
    for n in 0 .. 2
      for i in 1 .. 3
        for j in 1 .. 3
          for j_s in j+1 .. 3
            dimacs << "-#{3*m+1}#{3*n+j}#{k} -#{3*m+i}#{3*n+j_s}#{k} 0 \n"
            clauses += 1
          end
        end
      end
    end
  end
end

for k in 1 .. numbers
  for m in 0 .. 2
    for n in 0 .. 2
      for i in 1 .. 3
        for j in 1 .. 3
          for i_s in i+1 .. 3
            for j_s in 1 .. 3
            dimacs << "-#{3*m+1}#{3*n+j}#{k} -#{3*m+i_s}#{3*n+j_s}#{k} 0 \n"
            clauses += 1
            end
          end
        end
      end
    end
  end
end

dimacs = "c Created by sudoku dimacs generator \n" << dimacs
dimacs = "p cnf #{atoms} #{clauses} \n" << dimacs

puts dimacs
