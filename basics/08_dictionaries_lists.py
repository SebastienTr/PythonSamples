#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# This is a dict
toto = {"name": "Toto",
		"age": 67,
		}

# This is also a dict
titi = {"name": "Titi",
		"age": 43,
		}

# This is a list ... of dicts

mylist = (toto, titi)

print (mylist)

sorted_list = sorted(mylist, key=lambda k: k['age']) # Yeah this is a lambda function ;) => 05_functions.py

print (sorted_list)