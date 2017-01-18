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

    def prettyPrint( self, t ):
        qLen = len( t )
        retStr = "[ "
        for i in range( 1, qLen+1 ):
           retStr = retStr + str( i );
           if i < qLen:
              retStr = retStr + ","
        retStr = retStr + " ]"
        return retStr
        

    def moveDisks( self, s, d1, d2, nodeCount):
        print "a ",s,"\n"
        print "b ",d1,"\n"
        print "c ",d2,"\n"
        
        d2.append( s.pop() )
        if nodeCount == 1:
           return;
        
        d1.append( s.pop() )
        d1.append( d2.pop() )
        if nodeCount == 2:
           return;

        d2.append( s.pop() )
        s.append( d1.pop() )
        d2.append( d1.pop() )
        d2.append( s.pop() )
        

        

if __name__ == '__main__':

    n = int( sys.argv[1] )

    print n
    toh = TowerOfHanoi(n)

    print "before move in main...\n"
    print "a ",toh.a,"\n"
    print "b ",toh.b,"\n"
    print "c ",toh.c,"\n"

    print "pretty print a", toh.prettyPrint(toh.a)
    print "pretty print b", toh.prettyPrint(toh.b)
    print "pretty print c", toh.prettyPrint(toh.c)


    nodeCount = n % 3
    if nodeCount == 0:
       nodeCount = 3;

    toh.moveDisks( toh.a, toh.b, toh.c, nodeCount );

    print '---------------------\n'

    print "back in main...\n"
    print "a ",toh.a,"\n"
    print "b ",toh.b,"\n"
    print "c ",toh.c,"\n"

    print "pretty print a", toh.prettyPrint(toh.a)
    print "pretty print b", toh.prettyPrint(toh.b)
    print "pretty print c", toh.prettyPrint(toh.c)


