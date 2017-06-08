'''Animal Assignment, root Animal object, working with import
by: Troy Center, troycenter1@gmail.com, Coding Dojo Python fundamentals, June 2017
'''

#pylint: disable=C0103

class Animal(object):
    '''this is the root animal class
    '''
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self, distance):
        '''This function will decrement health by 1
        '''
        print "walking... for distance of", distance, ", -1 health per distance."
        self.health -= 1 * distance
        return self

    def run(self, distance):
        '''This function will decrement the health by 5
        '''
        print "running... for a distance of", distance, " -5 health per distance."
        self.health -= 5
        return self

    def displayHealth(self):
        '''This function will display the health of the animal
           it will also function in the child classes to return
           their health too.
        '''
        print "Current Health is: ", self.health
        return self
