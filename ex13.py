#sys is a dictionary that holds all the modules that have ever been imported since Python was started. 

#from sys import argv

#argv is an argument variable

# line 1 is called an import. this is how you add modules to your script. 
#script is another name for .py files 
#line 6 unpacks argv so that rather than holding all the arguments, it gets assigned to four variables you can work with in the order you list them in: script, first, second, and third. 

#script, first, second, third = argv

#print "the script is called:", script
#print "Your first variable is:", first
#print "Your second variable is:", second
#print "Your third variable is:", third

from sys import argv

ex13, egg, tadpole, frog, = argv

print "the script is called:", ex13
print "your first variable is:", egg
print "your second variable is:", tadpole
print "your third variable is:" , frog




#print "the story is called:", ex13.py
#print "first comes the:", egg
#print "When the egg hatches you get a:", tadpole
#print "Tadpole turns into a:", frog
#print "frogs on drugs:", roadkill

 

