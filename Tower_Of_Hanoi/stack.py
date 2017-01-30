class Stack:

     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

     def initializeStack(self, max):
         index = 0
         for x in range( max, 1 ):
             print "initialize x=,",x
             self.push( x )
             index += 1 

     def printStack(self):
         for x in range( self.size()-1, 0 ):
             print "x=,",x
             print( self.items[ x ] )

if __name__ == '__main__':
     s = Stack()
     s.initializeStack( 1 )
     s.printStack()

     print '------------\n'

     s.initializeStack( 10 )        
     s.printStack()
