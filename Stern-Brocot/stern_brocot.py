#!/usr/bin/python

import sys
from mediant import Mediant

### print 'Number of arguments:', len(sys.argv), 'arguments.'
### print 'Argument List:', str(sys.argv)

class SternBrocot:

	tree = []
	
	def __init__(self):
		print('1/1\n')
		
	def display_tree(self, tree):
		w = ''
		for item in tree:
			w = w + item.to_string() + ', '
			
		return w[:-2]
		
	def init_tree(self, l, r):	
		self.tree.append(l)
		self.tree.append(r)
		
		
	def next_farey(self, farey):
		return_tree = []
		farey_len = len(farey)
		for i in range(farey_len):
			if i+1 >= farey_len:
				return_tree.append( farey[i] )
				return return_tree
			l = farey[i]
			return_tree.append( l )
			r = farey[i+1]
			next_mediant  = Mediant(l.numerator + r.numerator, l.denominator + r.denominator)
			return_tree.append( next_mediant )
			
	def main(self):
		
		l = Mediant(0,1)
		r = Mediant(1,0)
		
		max_rows = int(sys.argv[1])
		
		self.init_tree(l, r)
		current_tree = self.tree
		counter = 1
		while True:
			next_row = self.next_farey(current_tree)
			print(self.display_tree(next_row) + '\n')
			current_tree = next_row
			counter += 1
			if counter > max_rows:
				sys.exit(0)

if __name__ == "__main__":
    # execute only if run as a script
	s = SternBrocot()
	s.main()
	
