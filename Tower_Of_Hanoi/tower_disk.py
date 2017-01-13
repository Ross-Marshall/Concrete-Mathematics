class Disk(object):
    id       = 0
    tower    = ''

    # The class "constructor" - It's actually an initializer 
    def __init__(self, id, tower):
        self.id       = id
	self.tower    = tower

    def print_disk(self):
       return "[ " + str(self.id) +" | " + self.tower + " ]"

    def __str__(self):
       return str( self.id )

def make_disk(id,tower):
    disk = Disk(id,tower)
    return disk

if __name__ == '__main__':
    d = Disk(3,'A') 
    print d.print_disk()

    d2 = make_disk( 6,'B' )
    print d2.print_disk()
 
