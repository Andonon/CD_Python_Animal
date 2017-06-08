'''Animal Assignment, child Dragon object, working with import
by: Troy Center, troycenter1@gmail.com, Coding Dojo Python fundamentals, June 2017
'''

#pylint: disable=C0103

from modules.allanimals import Animal

class Dragon(Animal):
    '''this is the child Dragon (of Animal class)
    '''
    def __init__(self, name, health=170):
        super(Dragon, self).__init__(name=name, health=health)
    def fly(self):
        '''If the dragon flies, he loses 10 health
        '''
        self.health += 10
        print "flying..... He's happy... and tired. Health went down by 10."
        return self
    def displayHealth(self):
        super(Dragon, self).displayHealth()
        '''In addition to the parent method.... print I'm a dragon!
        '''
        self.health += 1
        print "I'm a dragon. +1 health for self empowerment..."
        return self
        