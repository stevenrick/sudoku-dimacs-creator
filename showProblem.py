#!/usr/bin/python

import sys

def main():
	fname = sys.argv[1]

	lines = [word.split(',')[:-1] for line in open(fname, 'r') for word in line.split()]

	'''
	for line in open(fname, 'r'):
		for word in line.split():
			num = word.split(',')
			print num[:-1]

	print(lines)
	'''
	
	for row in lines:
		for val in row:
			print(str(val) + '\t'),
		print('\n'),

if __name__ == '__main__':
	main()