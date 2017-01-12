class Disk(object):
    id       = 0
    above    = 0
    below    = 0
    position = 0
    tower    = ''

    # The class "constructor" - It's actually an initializer 
    def __init__(self, id, above, below, position, tower):
        self.id       = id
        self.above    = above
        self.below    = below
	self.position = position
	self.tower    = tower

    def print_disk(self):
       return "[ " + str(self.id) +" | " + str(self.above) + " | " + str(self.below) + " | " + str(self.position) + " | " + self.tower + " ]"

def make_disk(id, above,below, position,tower):
    disk = Disk(id, above,below, position,tower)
    return disk



if __name__ == '__main__':
    d = Disk(1,2,3,4,'A') 
    print d.print_disk()

    d2 = make_disk( 5,6,7,8,'B' )
    print d2.print_disk()
 
