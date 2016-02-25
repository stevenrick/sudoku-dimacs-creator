#!/usr/bin/python
import sys

def pad(n, d):
	count = d
	s = n
	while(count > 0):
		s = '0' + s
		count -= 1
	return s

def main():
	# Get value of n from argument
	n = int(sys.argv[1])
	n2 = n * n
	size = len(str(n2)) # digits in n^2

	# read result of MiniSAT
        fname = sys.argv[2]
	file = open(str(fname), "r")
	data = file.read()
	file.close()

	# Skip 'SAT\n' and read the rest of the file
	# Fails when 'UNSAT\n' is the content
	if data == 'UNSAT\n':
		print("No solution found for the randomly generated initial state.")
		sys.exit()

	data = data[4:len(data)].split(' ')

	# Extract only the valid values
	cleaned = []

	for s in data:
		if s[0] != '-' and s!="0\n":# and len(s) == 3*size:
			#pad with 0 at the beginning to correct size
			v = s
			diff = 3*size - len(v)
			if(diff > 0):
				v = pad(v, diff)
			cleaned.append(v)

	#print(len(cleaned))

	# Put the valid values into a matrix
	sudoku = []

	for i in range(0, n2):
		sudoku.append([])

	for c in cleaned:
		unit = len(c)/3
		row = int(c[:unit])
		col = int(c[unit:2*unit])
		val = int(c[2*unit:])
		sudoku[row-1].insert(col-1, val)

	# Show the matrix
	for row in sudoku:
		for val in row:
			print(str(val) + "\t"),
		print("\n"),

if __name__ == '__main__':
	main()
