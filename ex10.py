#\t is a ASCII horizontal tab (TAB) 
#ASCII is the acronym for American Standard Code Interchange. It si a code for representing 128 english characters as numbers, with each letter assigned a number from 0 to 127. 

tabby_cat = "\tI'm tabbed in."
#\n is a new line
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

#the triple quote allows for a block of text to be written

#\\ prints a backslash
#\' prints a single quote
#\" double quote
#\a ASCII bell(BEL)
#\b ASCII backspace (BS)
#\f ASCII formfeed (FF)
#\n ASCII linefeed
#
#
#
#
#
#
#
#
#
#
#

fat_cat = """
I'll do a list:
\t*Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#use backslashes to escape certain characters from python. See examples:
 
print "I am 6'2\" tall." #escape double quote inside string
print 'I am 6\'2" tall.' #escape double quote inside string

while True:
	for i in ["/","-","|","\\","|"]:
		print "%s\r" % i,



