#!/bin/bash

if [ $# -ne 2 ]
	then
	echo "Usage: ./run.sh n r, where n is the size and r is the reduction method (1 or 2)."
	exit 1
fi

N="$1"
RED="$2"

if [[ RED -ne 1 && RED -ne 2 ]]
	then
	echo "Usage: ./run.sh n r, where r is either 1 or 2"
	exit 1
fi

SAT=minisat
INITIAL=initial.state
INPUT=sudoku.in
OUTPUT=sudoku.out

echo "Randomly generating the first row, first column and the main diagonal..."
python sudokuCreator.py $N > $INITIAL

echo "Generating DIMACS format input for $SAT ..."
python generate.py $N $RED $INITIAL > $INPUT

echo "Input file generated: $INPUT"
echo "Running SAT solver now..."
$SAT $INPUT $OUTPUT

echo "Showing Sudoku solution now..."
python show.py $N $OUTPUT
