#! /usr/bin/env python3
# -*- coding: utf-8 -*-

class You():
	"""This is you"""
	def __init__(self, name="", age=0):
		self.name = name # This line will call the name setter method which will set _name
		self.age = age; # This one will call the age setter method which will set _age

	
	@property # This is a getter
	def name(self):
		print ("get name")
		return self._name

	@name.setter # This is a setter
	def name(self, value):
		print ("set name")
		self._name = value.capitalize()

	@property # Beautiful
	def age(self):
		print ("get age")
		return self._age

	@age.setter # Isn't it ?
	def age(self, value):
		print ("set age")
		if value < 0:
			self._age = 0
		elif value > 100:
			print ("you're too old ! 100 is the maximum, sorry")
			self._age = 100
		else:
			self._age = value

	def __str__(self):
		return "Your name is {} and you're {} years old".format(self.name, self.age)

you = You(name="Titi") # New instance of You

you.age = 101 # 101 => 100
age = you.age

you.name = "toto" # capitalize "toto" => "Toto"
name = you.name

print (you)

# Let's try this ;) 
# help(you)
