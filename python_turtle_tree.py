import random

def tree(length):
	rand = (random.random() -0.5)*6
	rand_angle = (random.random() -0.5)*15
	real_length = length + rand
	width(length/10),go(real_length)
	if length > 10 and random.random()>0.1:
		turn(30+rand_angle )
		tree(real_length -5)
		turn(-30-rand_angle )
	if length > 10 and random.random()>0.05:
		turn(-30-rand_angle )
		tree(real_length -5)
		turn(30+rand_angle )
	go(-real_length)

tree(50)
