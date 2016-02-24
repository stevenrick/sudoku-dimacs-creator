sudoku-dimacs-creator
=====================

The program 'generate.py' creates an input file 'sudoku.in' in DIMACS format for minisat. The program 'show.py' reads minisat's solution from 'sudoku.out' and displays it in a matrix form. This works only if you have installed a SAT solver which reads inputs in DIMACS format.

You can call:

./run.sh n to solve a n^2 x n^2 Sudoku problem.
