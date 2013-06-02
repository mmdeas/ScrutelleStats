#!/usr/bin/env python
"""ScrutelleStats is a statistical tool for Latin and Ballroom competitions
which parses and caches information from Scrutelle."""

#Structure based on sergio-proxy by Ben Schmidt <supernothing@spareclockcycles.org>

__author__ = "Miguel Martinez de Aguirre"
__email__ = "miguel.aguirre@aguirredevelopment.co.uk"
__version__ = "0.1a"
__license__= """
Copyright 2013 Miguel Martinez de Aguirre <miguel.aguirre@aguirredevelopment.co.uk>
 
This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License as
published by the Free Software Foundation; either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307
USA
"""

import argparse

from views import *
view_classes = View.View.__subclasses__()

def initialiseViews():
	views = []
	for v in view_classes:
		try:
			views.append(v())
		except Exception, e:
			print "Failed to load view class '{}': {}".format(str(v), e)
	return views

def loadView(view):
	try:
		view.initialise(args)
		return True
	except NotImplementedError:
		print "View '{}' lacked initialise function.".format(view.name)
		return False

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="ScrutelleStats v{}".format(__version__))

	#Add generic options here when necessary
	
	#Initialise views
	views = initialiseViews()

	#Give subgroup to each view with options
	for v in views:
		try:
			if v.description == "":
				description = "Options for {}".format(v.name)
			else:
				description = v.description
			sgroup = parser.add_argument_subgroup(v.name, description)

			sgroup.add_argument("--{}".format(v.optname), action='store-true', 
				help="Show view '{}'", v.name)
			if v.has_opts:
				v.add_options(subgroup)
		except NotImplementedError:
			print "View '{}' claimed option support but didn't have it.".format(v.name)

	args = parser.parse_args()

	#Load views chosen on CLI
	load = []
	for v in views:
		if getattr(args, v.name):
			loadView(v)
			load.append(v)

	#TODO:
	#Do all the actual getting of information and passing it to views here

	#Cleanup on exit
	for v in load:
		v.finish()