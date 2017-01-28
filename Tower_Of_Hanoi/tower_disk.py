class Disk(object):
    id       = 0
    tower    = ''

    # The class "constructor" - It's actually an initializer 
    def __init__(self, id):
        self.id       = id

    def print_disk(self):
       return "[ " + str(self.id) + " ]"

    def pretty_print_disk(self):
       return "[ " + str(self.id) + " ]"

    def __str__(self):
       return str( self.id )

def make_disk(id):
    disk = Disk(id)
    return disk

if __name__ == '__main__':
    d = Disk(3) 
    print d.print_disk()

    d2 = make_disk( 6 )
    print d2.print_disk()
 
