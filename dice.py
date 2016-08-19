import random
import time

# setting minimum and maximum values for each die.
min = 1
max = 6

reroll = "yes"

while reroll == 'yes' or reroll == 'y':
	print "Rolling the dice..."
	time.sleep(1)
	die1 = random.randint(min,max)
	die2 = random.randint(min,max)
	total = die1 + die2

	print "Your rolled a %s and a %s, totaling %s." % (die1, die2, total)

	reroll = raw_input("Reroll? (y/n): \n")