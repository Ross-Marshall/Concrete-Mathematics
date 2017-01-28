import sys
from collections import deque
from Queue import PriorityQueue
import tower_disk
from stack import Stack

class TowerOfHanoi(object):

    moveCounter = 0;

    def moveTower(self, height, fromPole, toPole, withPole):
        if height >= 1:
            self.moveTower(height-1, fromPole, toPole, withPole)
            self.moveDisk(fromPole, toPole)
            self.moveTower(height-1, withPole, toPole, fromPole)
           
    def moveDisk( self, fp, tp ):
        print "moving disk from ", fp, " to ", tp  
        self.moveCounter += 1          

if __name__ == '__main__':

    if len( sys.argv ) == 1:
         print "USAGE: tower_of_hanoi <tower length>\n"
         sys.exit(-1)


    n = int( sys.argv[1] )
    if n <= 0:
         print "ERROR: Tower length must be 1 or greater\n"
         sys.exit(-1)

    
    toh = TowerOfHanoi()

    if n % 2 == 1:
        toh.moveTower( n, "A", "C", "B" )
    else:
        toh.moveTower( n, "A", "B", "C" )

    print "Done...  Total number of moves = ",toh.moveCounter,"\n"
