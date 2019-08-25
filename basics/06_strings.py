#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# The most simple way to declare a string
str1 = "the answer to life the universe and everything"

# The string object have a .format() method
# It take as parameters the variables declared with {}
str2 = "{} is {} !".format(str1, 42)

# You can also name your parameters
# It can be pretty confortable to read in that way
str3 = "{string} is {number} !".format(string=str1, number=42)

# Let's print now
print (str1)
print (str2)
print (str3)

# The string object have some other nice secrets, read the doc
print ("Upper : ", str3.upper())
print ("Capitalize : ", str3.capitalize())
print ("The universe : ", str1[19:31])

# Then you can try this by yourself
### str1[10:] str1[:10] str1[10:-2] ...

# RTFM ;) https://docs.python.org/3/library/string.html
