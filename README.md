sudoku-dimacs-creator
=====================

The program 'generate.py' creates an input file 'sudoku.in' in DIMACS format for minisat. The program 'show.py' reads minisat's solution from 'sudoku.out' and displays it in a matrix form. This works only if you have installed minisat.

You can call:

$ ./run.sh n r

to solve a n^2 x n^2 Sudoku problem using reduction method r (r = 1 or 2).
