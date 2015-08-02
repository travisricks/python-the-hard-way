name = 'Travis D. Ricks'
age = 33 # yeah
height = 73 # inches
weight = 180 # lie
eyes = 'Hazel'
teeth = 'White'
hair = 'Thin'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the cola." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)

# %s, %r, and %d are called 'formatters'.
# To round a floating point number use 'round()'. e.g. round(1.7333)