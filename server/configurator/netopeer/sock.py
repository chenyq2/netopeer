#!/usr/bin/python
# -*- coding:utf-8 -*-

import curses
import os
import nc_module
import messages
import config

class sock(nc_module.nc_module):
	name = 'Intercommunication'
			
	def find(self):
		return(True)

	def get(self):
		return(True)

	def update(self):
		return(True)

	def paint(self, window, focus, height, width):
		tools = []
		window.addstr('For intercommunication between Netopeer server and agents is used: UNIX sockets\n\n')
		
		window.addstr('To change the values below, recompile the Netopeer server\nwith the configure options --with-user and --with-group.\n\n')
		window.addstr('Allowed user to start the Netopeer server:\n')
		window.addstr('  {s}\n\n'.format(s=config.options['user']))
			
		window.addstr('Allowed group to connect to the Netopeer server:\n')
		window.addstr('  {s}\n\n'.format(s=config.options['group']))
		
		return(tools)

	def handle(self, stdscr, window, height, width, key):
		return(True)