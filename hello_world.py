#!/usr/bin/env python
from math import pi	
def hello_world():
	print('Hello, world!')
	
class ShibaInu:
	def __init__(self, weight, name):	
		self.tail='curly'
		self.ears='pointy'
		self.weight=weight
		self.name=name

	def introduce(self):
		print('HI! My name is {name}!!! My tail is {tail}, my ears are {ears}, and I weigh {weight} pounds.'.format(
				name=self.name, tail=self.tail, ears=self.ears, weight=self.weight))
	def beg(self):
		print('Please could I have some of that?')
	def howl(self):
		print('AROooooOOOOOooOoOOoOOOOoooOOOOOOOoooo!')
		
class SpherePet:
	def __init__(self, position, radius):
		self.position=position
		self.radius=radius	
		
	def tell_stats(self):
		print('My volume is {volume} and my position is {position}.'.format(volume=(4/3)*pi*(self.radius**3), position=self.position))
		
		