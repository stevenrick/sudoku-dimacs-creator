#!/usr/bin/python
import sys

def literal(i, j, k, n2):
	return fit(i, n2) + fit(j, n2) + fit(k, n2)

def fit(n, n2):
	fitn = ""
	diff = len(str(n2)) - len(str(n))
	for i in range(0, diff):
		fitn += "0"
	fitn += str(n)
	return fitn

def reduction2(n):
    n2      = n * n
	atoms   = n2 * n2 * n2
	clauses = 0
	dimacs  = ""
	digits = len(str(n2))

	'''UNDER CONSTRUCTION: NEED TO ADD OTHER CLAUSES TOO'''
	dimacs += "c At least one number in each entry\n"
	for i in range(1, n2 + 1):
	  for j in range(1, n2 + 1):
	    for k in range(1, n2 + 1):
	      dimacs += literal(i, j, k, n2) + " "
	    dimacs += "0 \n"
	    clauses += 1
	
	
	dimacs += "c A number is not repeated in a row\n"
	for i in range(1, n2 + 1):
	  for j in range(1, n2 + 1):
	    for k in range(1, n2 + 1):
	      for j_s in range(j+1, n2 + 1):
	        dimacs += "-" + literal(i, j, k, n2) + " -" + literal(i, j_s, k, n2) + " 0 \n"
	        clauses += 1
	
	dimacs += "c A number is not repeated in a column\n"
	for i in range(1, n2 + 1):
	  for j in range(1, n2 + 1):
	    for k in range(1, n2 + 1):
	      for i_s in range(i+1, n2 + 1):
	        dimacs += "-" + literal(i, j, k, n2) + " -" + literal(i_s, j, k, n2) + " 0 \n"
	        clauses += 1


	dimacs += "c A number is not repeated in a " + str(n) + "*" + str(n) + " sub-matrix\n"
	for k in range(1, n2+1):
		for x in range(0, n):
			for y in range(0, n):
				for i in range(1, n+1):
					for j in range(1, n+1):
						for z in range(j+1, n+1):
							dimacs += "-" + literal(n*x + i, n*y + j, k, n2) + " -" + literal(n*x + i, n*y + z, k, n2) + " 0 \n"
							clauses += 1

	for k in range(1, n2+1):
		for x in range(0, n):
			for y in range(0, n):
				for i in range(1, n+1):
					for j in range(1, n+1):
						for z in range(i+1, n+1):
							for w in range(1, n+1):
								dimacs += "-" + literal(n*x + i, n*y + j, k, n2) + " -" + literal(n*x + z, n*y + w, k, n2) + " 0 \n"
								clauses += 1


	dimacs = "c Created by Sudoku Dimacs Creator \n" + dimacs
	dimacs = "p cnf " + str(atoms) + " " + str(clauses) + " \n" + dimacs

	print(dimacs),

def reduction2(n):
	n2      = n * n
	atoms   = n2 * n2 * n2
	clauses = 0
	dimacs  = ""
	digits = len(str(n2))

	dimacs += "c At least one number in each entry\n"
	for i in range(1, n2 + 1):
	  for j in range(1, n2 + 1):
	    for k in range(1, n2 + 1):
	      dimacs += literal(i, j, k, n2) + " "
	    dimacs += "0 \n"
	    clauses += 1
	
	
	dimacs += "c A number is not repeated in a row\n"
	for i in range(1, n2 + 1):
	  for j in range(1, n2 + 1):
	    for k in range(1, n2 + 1):
	      for j_s in range(j+1, n2 + 1):
	        dimacs += "-" + literal(i, j, k, n2) + " -" + literal(i, j_s, k, n2) + " 0 \n"
	        clauses += 1
	
	dimacs += "c A number is not repeated in a column\n"
	for i in range(1, n2 + 1):
	  for j in range(1, n2 + 1):
	    for k in range(1, n2 + 1):
	      for i_s in range(i+1, n2 + 1):
	        dimacs += "-" + literal(i, j, k, n2) + " -" + literal(i_s, j, k, n2) + " 0 \n"
	        clauses += 1


	dimacs += "c A number is not repeated in a " + str(n) + "*" + str(n) + " sub-matrix\n"
	for k in range(1, n2+1):
		for x in range(0, n):
			for y in range(0, n):
				for i in range(1, n+1):
					for j in range(1, n+1):
						for z in range(j+1, n+1):
							dimacs += "-" + literal(n*x + i, n*y + j, k, n2) + " -" + literal(n*x + i, n*y + z, k, n2) + " 0 \n"
							clauses += 1

	for k in range(1, n2+1):
		for x in range(0, n):
			for y in range(0, n):
				for i in range(1, n+1):
					for j in range(1, n+1):
						for z in range(i+1, n+1):
							for w in range(1, n+1):
								dimacs += "-" + literal(n*x + i, n*y + j, k, n2) + " -" + literal(n*x + z, n*y + w, k, n2) + " 0 \n"
								clauses += 1


	dimacs = "c Created by Sudoku Dimacs Creator \n" + dimacs
	dimacs = "p cnf " + str(atoms) + " " + str(clauses) + " \n" + dimacs

	print(dimacs),

def main():
	n = int(sys.argv[1])
	reduction = int(sys.argv[2])
	
	if reduction == 1:
		reduction1(n)
	elif reduction == 2:
		reduction2(n)

if __name__ == '__main__':
	main()
