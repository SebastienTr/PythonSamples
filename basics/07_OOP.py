#! /usr/bin/env python3
# -*- coding: utf-8 -*-

class You():
	"""This is you"""
	def __init__(self, name="", age=0):
		self._name = name # This line will call the name setter method which will set _name
		self._age = age; # This one will call the age setter method which will set _age

	def _getName(self):
		print ("get name")
		return self._name

	def _setName(self, value):
		print ("set name")
		self._name = value.capitalize()

	def _getAge(self):
		print ("get age")
		return self._age

	def _setAge(self, value):
		print ("set age")
		if value < 0:
			self._age = 0
		elif value > 100:
			print ("you're too old ! 100 is the maximum, sorry")
			self._age = 100
		else:
			self._age = value

	name = property(_getName, _setName, None, 'I am the name')
	age = property(_getAge, _setAge, None, 'I am the age')

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
