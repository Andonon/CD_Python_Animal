'''Animal Assignment, root Animal object, working with import
by: Troy Center, troycenter1@gmail.com, Coding Dojo Python fundamentals, June 2017
'''
#pylint: disable=C0103

from modules.allanimals import Animal
from modules.dogs import Dog
from modules.dragon import Dragon

Troy = Animal('Troy', 100).displayHealth().walk(2).walk(1).walk(1).run(2).run(1).displayHealth()
Jake = Dog('Jake', 150).displayHealth().walk(1).walk(1).walk(1).run(2).run(2).pet().displayHealth()
Pete = Dragon("Pete", 100).displayHealth().displayHealth().displayHealth()

print "Trying Troy.pet, trying to pet an Animal... "
while True:
    try:
        Troy.pet() #should generate an error.
        break
    except AttributeError:
        print "This was expected to fail... You cannot pet an Animal, only Dogs. That's wierd."
        break

print "Trying Troy.fly, trying to fly an Animal... "
while True:
    try:
        Troy.fly() #should generate an error.
        break
    except AttributeError:
        print "This was expected to fail... Generally, Animals don't fly, only Dragons can fly."
        break

print "This next line for displayHealth should NOT show 'I'm a dragon...'"
Troy.displayHealth() #should not print "I'm a dragon"

while True:
    try:
        Jake.fly() #should generate an error.
        break
    except AttributeError:
        print "This was expected to fail... Jake is a dog, dog's cannot fly."
        break
