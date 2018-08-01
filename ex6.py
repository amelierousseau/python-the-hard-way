#the 10 replaces the %d.
x = "there are %d types of people." % 10

#define the variables as strings
binary = "binary"
do_not = "don't"

#plug in the variables into the string using %s
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# %r is the 'raw' data of teh variable, while %s and %d is used to display to users
print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."
#adding two strings tog w a + is called "concatenating" the strings

print w + e

v = "A cat walked into a bar"
b = " and immediately threw up on the floor."

print v + b



