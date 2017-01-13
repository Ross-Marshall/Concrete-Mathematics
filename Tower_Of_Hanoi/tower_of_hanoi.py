import sys
from collections import deque
import tower_disk

class TowerOfHanoi(object):

    a = deque([])
    b = deque([])
    c = deque([])
    
    def __init__(self, n):
	for x in range(n, 0, -1):
	    self.a.append( tower_disk.Disk( x, 'A' ) )
            print "a = ", self.a
         

if __name__ == '__main__':

    n = int( sys.argv[1] )
    print n
    toh = TowerOfHanoi(n)

    i = toh.a.pop()
    print "Now a = ", toh.a
    print "i = ", i

    i = toh.a.pop()
    print "Now a = ", toh.a
    print "i = ", i

    i = toh.a.pop()
    print "Now a = ", toh.a
    print "i = ", i
    
