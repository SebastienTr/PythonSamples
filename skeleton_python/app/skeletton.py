#! /usr/bin/env python3
# -*- coding: utf-8 -*-

class Skeletton():
	"""Free your mind :)"""
	def __init__(self, string = "Hello World !"):
		super(Skeletton, self).__init__()
		self.string = string
		
	def run(self):
		print (self.string)


def main():
	skeletton = Skeletton()
	skeletton.run()
