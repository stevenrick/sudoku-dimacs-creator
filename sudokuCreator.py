#!/usr/bin/python
import sys
import random


def main():
    #read input n
    n = int(sys.argv[1])
    size = n*n

    if n == size:
        return '1'


    #setup first row randomly
    sudoku_row = random.sample(range(1,size+1), size)

    #setup first col randomly, removing first el shared with first row
    temp_sudoku_col = random.sample(range(1,size+1), size)
    temp_sudoku_col.remove(sudoku_row[0])

    #evaluate first sub-matrix and shuffle if needed
    col_invalid = []
    for x in range(1,n):
        col_invalid.append(sudoku_row[x])

    while(set(temp_sudoku_col[0:n-1]).intersection(set(col_invalid))):
        random.shuffle(temp_sudoku_col)
    sudoku_col = [sudoku_row[0]] + temp_sudoku_col

    #build and fill the diagonal for each sub-matrix
    for x in range(0,n):
        if x == 0:
            temp = [sudoku_row[0]]
            sudoku_dia = [sudoku_row[0]]
            for i in range(x*n,x*n+n):
                temp += [sudoku_row[i]]+[sudoku_col[i]]
            for i in range(1,n):
                rand = random.sample(range(1,size+1), 1)[0]
                while rand in temp:
                    rand = random.sample(range(1,size+1), 1)[0]
                sudoku_dia += [rand]
                temp += [rand]
        else:
            sub = []
            for i in range(x*n,x*n+n):
                temp = []
                temp += [sudoku_row[i]]+[sudoku_col[i]]
                rand = random.sample(range(1,size+1), 1)[0]
                while rand in temp or rand in sub:
                    rand = random.sample(range(1,size+1), 1)[0]
                sudoku_dia += [rand]
                sub += [rand]

    #build final matrix
    space = ' '*len(str(size))
    puzzle = [[[space] for _ in range(size)] for _ in range(size)]

    for n in range(len(sudoku_row)):
        puzzle[0][n] = [str(sudoku_row[n]).rjust(len(str(size)))]
    for n in range(len(sudoku_col)):
        puzzle[n][0] = [str(sudoku_col[n]).rjust(len(str(size)))]
    for n in range(len(sudoku_dia)):
        puzzle[n][n] = [str(sudoku_dia[n]).rjust(len(str(size)))]

    #visualize matrix nicely
    for row in puzzle:
        print row
    print ''

    #output matrix to text file
    output = ""
    for rows in range(len(puzzle)):
        for cols in range(len(puzzle[rows])):
            output += puzzle[rows][cols][0].strip()+","
        output += "\n"
    return output


if __name__ == '__main__':
    print main()
