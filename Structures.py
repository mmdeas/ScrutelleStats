class Couple:
	def __init__(self, name, university, number):
		self.name = name
		self.university = university
		self.number = number

class Round:
	def __init__(self, dance, round, marks):
		self.dance = dance
		self.round = round
		self.marks = marks

class Event:
	def __init__(self, name, rounds, judges):
		self.name = name
		self.rounds = rounds
		self.judges = judges

class Competition:
	def __init__(self, name, year):
		self.name = name
		self.year = year