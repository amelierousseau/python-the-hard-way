from sys import argv

script, user_name = argv
prompt = '"  "'

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you betray me %s?" % user_name
betrays = raw_input (prompt)

print "Where do you forgive %s?" % user_name
forgives = raw_input (prompt)

print "What kind of computer do you have?"
computer = raw_input (prompt)

print "How often do you betray from your computer?"
betrays = raw_input (prompt)

print """
Alright, so you said %r about betraying me.
You forgive in %r. Not sure where that is.
You have a %r computer. And you betray %r from that computer. Nice.
""" % (betrays, forgives, computer, betrays)


