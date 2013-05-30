class Couple:
	"""Describes a couple dancing at a specific competition."""
	def __init__(self, name, university, number):
		"""	name	(String) Name of the couple at the competition. Generally of the form
					Lead Name & Follower Name
			university	(String) Name of the university the couple dance for.
			number	(Integer) The number of the couple at the competition.
		"""
		self.name = name
		self.university = university
		self.number = number

class Round:
	"""Describes a round of an event at a competition."""
	def __init__(self, dance, round, marks):
		# Should round change to String for 'Final' etc? Should be as in Scrutelle.
		# Should dance change to Event? Look up weak references in python.
		"""	dance	(String) Name of the event as it appears in Scrutelle.
			round	(Integer) Number of the round. Starts at 1.
			marks	(Dictionary) {Couple: Integer} Maps Couple objects to
					number of marks they got.
		"""
		self.dance = dance
		self.round = round
		self.marks = marks

class Event:
	"""Describes an event at a competition."""
	def __init__(self, name, rounds, judges):
		"""	name	(String) Name of the event as it appears in Scrutelle.
			rounds	(List) [Round, ...] List of Round objects for this event.
			judges	(List) [String, ...] List of Judges' names for this event.
		"""
		self.name = name
		self.rounds = rounds
		self.judges = judges

class Competition:
	"""Describes a competition."""
	def __init__(self, name, date, events=[]):
		"""	name	(String) Name of the competition.
			date	(date|String) Date the competition was held. Can be datetime.date
					object or string. If it is a string, it should be in dd/mm/yy
					format.
			events	(List) [Event, ...] List of Event objects.
		"""
		self.name = name
		if type(date) == datetime.date:
			self.date = date
		else:
			self.date = datetime.datetime.strptime(date, '%d/%m/%y').date()
		self.events = events