import sys
from collections import deque
from Queue import PriorityQueue
import tower_disk
import Stack

class TowerOfHanoi(object):

    a =  None # Stack()
    b =  None #Stack()
    c =  None #nul #Stack()

    aLength = 0
    bLength = 0
    cLength = 0

    moves = 0
    
    def __init__(self, n):
	for x in range(1, n+1):
	    self.a.push( tower_disk.Disk( x ) )

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
        self.aLength = size( self.a )
        self.bLength = size( self.b )
        self.cLength = size( self.c )

    def moveTower(self, height, fromPole, toPole, withPole):
        if height >= 1:
            self.moveTower(height-1, fromPole, toPole, withPole)
            self.moveDisk(fromPole, toPole)
            self.moveTower(height-1, withPole, toPole, fromPole)
           
    def moveDisk( self, fromPole, toPole ):
        print "moving disk from ", self.prettyPrint(fromPole), " to ", self.prettyPrint(toPole) 
        toPole.push( fromPole.pop() )
        
        
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
    toh.a = Stack()
    toh.b = Stack()
    toh.c = Stack()

    if n % 2 == 1:
        toh.moveTower( n, toh.a, toh.c, toh.b )
    else:
        toh.moveTower( n, toh.a, toh.b, toh.c )

    toh.prettyPrintTowers()

    print "Done...\n"

