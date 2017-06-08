'''Animal Assignment, child Dog object, working with import
by: Troy Center, troycenter1@gmail.com, Coding Dojo Python fundamentals, June 2017
'''

#pylint: disable=C0103

from modules.allanimals import Animal

class Dog(Animal):
    '''this is the child Dog (of Animal class)
    '''
    def __init__(self, name, health=150):
        super(Dog, self).__init__(name=name, health=health)
    def pet(self):
        '''If you pet the dog, he heals by 5 health
        '''
        print "petting the dog... He's happy... gain 5 health!"
        self.health += 5
        return self
    