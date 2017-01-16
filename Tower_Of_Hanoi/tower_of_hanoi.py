import sys
from collections import deque
import tower_disk

class TowerOfHanoi(object):

    a = deque([])
    b = deque([])
    c = deque([])
    
    def __init__(self, n):
	for x in range(1, n+1):
	    self.a.append( tower_disk.Disk( x, 'A' ) )

    def moveDisk( self, s, d1, d2, nodeCount ):
        print "a ",s,"\n"
        print "b ",d1,"\n"
        print "c ",d2,"\n"
        d1.append( s.pop() )
        

if __name__ == '__main__':

    n = int( sys.argv[1] )

    print n
    toh = TowerOfHanoi(n)

    print "Now a = ", toh.a
    for node in toh.a:
        print str( node )

    nodeCount = n % 3
    if nodeCount == 0:
       nodeCount = 3;

    toh.moveDisk( toh.a, toh.b, toh.c, nodeCount );

    print "back in main...\n"
    print "a ",toh.a,"\n"
    print "b ",toh.b,"\n"
    print "c ",toh.c,"\n"

    for node in toh.a:
        print str( node )

    print '---------------------\n'

    for node in toh.b:
        print str( node )



