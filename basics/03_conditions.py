#! /usr/bin/env python3
# -*- coding: utf-8 -*-

theAnswer = 42

if theAnswer >= 0:
	print ("the", end=" ")
elif theAnswer < 42:
	print ("UNIVERSE !")
else:
	print ("No :)")

if theAnswer % 2 == 0:
	print ("answer", end=" ")

if theAnswer >= 43 or theAnswer < 43:
	print ("to", end=" ")

if theAnswer is not False:
	print ("life", end=", ")

if theAnswer is not None:
	print ("the", end=" ")

if theAnswer in [1, 2, 3, 42]:
	print ("universe", end=" ")

if theAnswer not in [1, 2, 3]:
	print ("and", end=" ")

if theAnswer in (1, 42):
	print ("everything")
