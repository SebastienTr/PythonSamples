#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict

class Observable:
	def __init__(self):
		self.observers = defaultdict(list)

	def notify_observers(self, event):
		for obs in self.observers[event]:
			obs.notify(self)
			
	def add_observer(self, obs):
		if not hasattr(obs, 'notify'):
			raise ValueError("First argument must be object with notify method")
		# self.observers.append(obs)
		print ('###', obs.type)
		self.observers[obs.type].append(obs)
		print ("OK")

class Speed:
	def __init__(self):
		self.type = "speed"

	def notify(self, subject):
		print("speed", subject.speed)

class Rpm:
	def __init__(self):
		self.type = "rpm"

	def notify(self, subject):
		print("rpm", subject.rpm)

class Car(Observable):
	def __init__(self):
		Observable.__init__(self)
		self.speed = 0
		self.rpm = 0
		self.gearbox = [.016, 0.038, .038, .042]
		self.gearbox_speed  = 0

	def accelerate(self):
		self.rpm += 1000
		self.speed = self.rpm * self.gearbox[self.gearbox_speed]
		self.notify_observers("speed")
		self.notify_observers("rpm")

	def downshift(self):
		if self.gearbox_speed > 0:
			self.gearbox_speed -= 1
			self.speed = self.rpm * self.gearbox[self.gearbox_speed]
			self.notify_observers("speed")

	def upshift(self):
		if self.gearbox_speed < 3:
			self.gearbox_speed += 1
			self.speed = self.rpm * self.gearbox[self.gearbox_speed]
			self.notify_observers("speed")

if __name__ == "__main__":
	car = Car()
	car.add_observer(Speed())
	car.add_observer(Rpm())

	car.accelerate()
	car.upshift()
	car.upshift()
	car.downshift()