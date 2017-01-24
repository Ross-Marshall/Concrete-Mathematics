import sys
from collections import deque
from Queue import PriorityQueue
import tower_disk

class TowerOfHanoi(object):

    a = []
    b = []
    c = []

    aLength = 0
    bLength = 0
    cLength = 0

    moves = 0
    
    def __init__(self, n):
	for x in range(1, n+1):
	    self.a.insert( 0, tower_disk.Disk( x, 'A' ) )

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

    def refreshTowerLengths(self):
        self.aLength = len( self.a )
        self.bLength = len( self.b )
        self.cLength = len( self.c )

    def traverse(self, current):
       pass
        
    def checkTower(self, n, check):
       if n <= check:
           print "pretty print a", toh.prettyPrint(toh.a)
           print "pretty print b", toh.prettyPrint(toh.b)
           print "pretty print c", toh.prettyPrint(toh.c)
           print "checkTower: Exiting..."
           sys.exit()

    def prettyPrintTowers(self):
        print "pretty print a", self.prettyPrint(toh.a)
        print "pretty print b", self.prettyPrint(toh.b)
        print "pretty print c", self.prettyPrint(toh.c)

    def moveDisks( self, s, d1, d2, nodeCount):
        if len( s ) == 0:
           d2.append( s[0] )
        else:
           d2.insert( 0, s[0] )
        del s[0]

        self.moves += 1
        if nodeCount == 1:
           return;
        
        d1.insert( 0, s[0] )
        del s[0]

        d1.insert( 0,  d2[0] )
        del d2[0]

        print "n =", n
        self.moves += 2
        if nodeCount == 2:
           return;

        d2.insert( 0,  s[0] )
        del s[0]

        s.insert( 0,  d1[0] )
        del d1[0]

        d2.insert( 0,  d1[0] )
        del d1[0]

        d2.insert( 0,  s[0] )
        del s[0]

        self.moves += 4
            

if __name__ == '__main__':

    if len( sys.argv ) == 1:
         print "USAGE: tower_of_hanoi <tower length>\n"
         sys.exit(-1)


    n = int( sys.argv[1] )
    if n <= 0:
         print "ERROR: Tower length must be 1 or greater\n"
         sys.exit(-1)

    toh = TowerOfHanoi(n)
    toh.prettyPrintTowers()

    print "---------------------------------"

    print "n = ", n
    if n >= 1 and n <= 3:
        print "move disk...\n"
        toh.moveDisks( toh.a, toh.b, toh.c, n )   
       
    toh.prettyPrintTowers() 
    sys.exit()
    
    nodeCount = n % 3
    if nodeCount == 0:
       nodeCount = 3;

    #nodeCount = 3;
    toh.moveDisks( toh.a, toh.b, toh.c, nodeCount )

    print '---------------------\n'
    if n <= 3:
        print "pretty print a", toh.prettyPrint(toh.a)
        print "pretty print b", toh.prettyPrint(toh.b)
        print "pretty print c", toh.prettyPrint(toh.c)
        sys.exit()
    print "N = ", n, " Moves = ", toh.moves

    nodeCount = 3;
    toh.moveDisks( toh.a, toh.c, toh.b, nodeCount )

    nodeCount = 3;
    toh.moveDisks( toh.c, toh.b, toh.a, nodeCount )

    nodeCount = 3;
    toh.moveDisks( toh.a, toh.b, toh.c, nodeCount )
    toh.checkTower(n, 6)
    

    toh.moveDisks( toh.c, toh.a, toh.b, nodeCount )
    print "pretty print a", toh.prettyPrint(toh.a)
    print "pretty print b", toh.prettyPrint(toh.b)
    print "pretty print c", toh.prettyPrint(toh.c)
    toh.moveDisks( toh.a, toh.b, toh.c, nodeCount )
    print "pretty print a", toh.prettyPrint(toh.a)
    print "pretty print b", toh.prettyPrint(toh.b)
    print "pretty print c", toh.prettyPrint(toh.c)
    toh.moveDisks( toh.b, toh.a, toh.c, nodeCount )
    print "pretty print a", toh.prettyPrint(toh.a)
    print "pretty print b", toh.prettyPrint(toh.b)
    print "pretty print c", toh.prettyPrint(toh.c)
    toh.moveDisks( toh.c, toh.b, toh.a, nodeCount )
    print "pretty print a", toh.prettyPrint(toh.a)
    print "pretty print b", toh.prettyPrint(toh.b)
    print "pretty print c", toh.prettyPrint(toh.c)
    toh.moveDisks( toh.b, toh.a, toh.c, nodeCount )
    print "pretty print a", toh.prettyPrint(toh.a)
    print "pretty print b", toh.prettyPrint(toh.b)
    print "pretty print c", toh.prettyPrint(toh.c)
    toh.moveDisks( toh.a, toh.b, toh.c, nodeCount )
    print "pretty print a", toh.prettyPrint(toh.a)
    print "pretty print b", toh.prettyPrint(toh.b)
    print "pretty print c", toh.prettyPrint(toh.c)       
    print "N = ", n, " Moves = ", toh.moves


