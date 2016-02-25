sudoku-dimacs-creator
=====================

Minimum Requirements:
- Python
- minisat
- Bash

First, 'generateSudoku.py' randomly generates the first row, column and main diagonal and stores the result in 'initial.state'. Then, the program 'generate.py' reads 'initial.state' and creates the file 'sudoku.in' in DIMACS format as input for minisat. The program 'show.py' reads minisat's solution from 'sudoku.out' and displays it in a matrix form. This works only if you have installed minisat.

You can call:

$ ./run.sh n r

to solve a n^2 x n^2 Sudoku problem using reduction method r (r = 1 or 2).
