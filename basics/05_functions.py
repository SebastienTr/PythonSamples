#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# The default value of end is "\n", so this parameter is optional
def myPrintParam(param, end="\n"):
	print (param, end=end)

# Will automaticaly print a new line  after the string
myPrintParam("Hello world !")

g = lambda x: x * 2
# This is a function declaration in one line
# It take x as parameter and return x * 2

myPrintParam(g(21), end="\t(21 * 2 = 42)\n")
