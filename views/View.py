#Copyright 2013 Miguel Martinez de Aguirre <miguel.aguirre@aguirredevelopment.co.uk>

"""The base View class. All views must subclass this one to be accessible.
Shows the various methods which can be called on a view."""

class View(object):
	name = "Generic View"
	description = ""
	optname = "generic"
	has_opts = False

	def __init__(self):
		"""Called on view instantiation. Probably don't need this"""
		pass

	def initialize(self,options):
		"""Called if view is enabled, passed the options namespace"""
		self.options = options

	def add_options(options):
		"""Add your options to the options parser"""
		raise NotImplementedError

	def finish(self):
		"""This will be called when shutting down."""
		pass