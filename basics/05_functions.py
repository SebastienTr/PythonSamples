#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def myPrintParam(param, end="\n"):
	print (param, end=end)

myPrintParam("Hello world !")

g = lambda x: x * 2 # Don't worry, you will understand just after ;)

myPrintParam(g(21), end=" => 21 * 2 == 42\n")

