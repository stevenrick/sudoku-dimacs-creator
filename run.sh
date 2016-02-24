#!/bin/bash

N="$1"
SAT=minisat
INPUT=sudoku.in
OUTPUT=sudoku.out

python generate.py $N > $INPUT
$SAT $INPUT $OUTPUT
python show.py $N $OUTPUT
