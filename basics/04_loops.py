#! /usr/bin/env python3
# -*- coding: utf-8 -*-

mylist = ("Hello", "my name is", "toto", "i'm", 42, "years old")

for elem in mylist:
	print (elem, end=" ")

print () ## I just want a new line

# enumerate(mylist) return a list with the mylist's keys
for i, elem in enumerate(mylist):
	print (i, elem)

print ("\n==> Python bonus\n")

[print (str(elem).replace("toto", "Saibo").replace("42", "25").upper(), end=" ") for elem in mylist]

