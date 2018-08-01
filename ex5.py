name = 'Amelie C. Rousseau'
age = 30 #not a lie
pounds = 0.45359
kilos = 2.2 * pounds
height = 67 #inches
weight = 150 #lbs
weight2 = 150/2.2 #pounds to kilos 
height2 = 67 * 2.5
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "I am %r centimeters tall." % height2
print "I am %r kilos heavy." % weight2
print "Actually that's not too heavy." 
print "I have %s eyes and %s hair." % (eyes, hair)
print "my teeth are usually %s depending on the coffee." % teeth

#this line is tricky, try to get it exactly right.
print "If I add %r, %r, and %r I get %r." % (
	age, height2, weight2, age + height2 + weight2)

