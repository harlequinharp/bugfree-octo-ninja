#!/usr/bin/env python
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