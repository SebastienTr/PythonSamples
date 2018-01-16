#! /usr/bin/env python3
# -*- coding: utf-8 -*-

str1 = "the answer to life the universe and everything"

str2 = "{} is {} !".format(str1, 42)

str3 = "{string} is {number} !".format(string=str1, number=42)

print (str1)
print (str2)
print (str3)

print ("Upper : ", str3.upper())
print ("Capitalize : ", str3.capitalize())
print ("The universe : ", str1[19:31])

# Then let's see what is this : str1[10:] str1[:10] str1[10:-2] ...