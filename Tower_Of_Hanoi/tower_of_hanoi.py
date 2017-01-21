import sys
from collections import deque
from Queue import PriorityQueue
import tower_disk

class TowerOfHanoi(object):

    a = []
    b = []
    c = []

    moves = 0
    
    def __init__(self, n):
	for x in range(1, n+1):
	    self.a.append( tower_disk.Disk( x, 'A' ) )

    def prettyPrint( self, t ):
        qLen = len( t )
        counter = 1
        retStr = "[ "
        for i in t:
           retStr = retStr + str( i );
           counter += 1
           if counter <= qLen:
              retStr = retStr + ", "
        retStr = retStr + " ]"
        return retStr
        

    def moveDisks( self, s, d1, d2, nodeCount):
        print "moveDisks a ",s,"\n"
        print "moveDisks b ",d1,"\n"
        print "moveDisks c ",d2,"\n"
        
        d2.append( s[0] )
        del s[0]
        self.moves += 1
        if nodeCount == 1:
           return;
        
        d1.append( s[0] )
        del s[0]

        d1.append( d2[0] )
        del d2[0]

        self.moves += 2
        if nodeCount == 2:
           return;

        d2.append( s[0] )
        del s[0]
        s.append( d1[0] )
        del d1[0]
        d2.append( d1[0] )
        del d1[0]
        d2.append( s[0] )
        del s[0]
        self.moves += 4
            

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

    print "N = ", n, " Moves = ", toh.moves


