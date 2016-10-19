'''
Main file responsible for playing the audio messages
'''
import random
import os

from app import (app,logging, db, settings)
from flask import (make_response, request)

from models.voice import Voice
from models.contacts import Contacts

@app.route('/voice', methods= ['POST'])
def voice_callback():
	isActive     = request.values.get('isActive', None)
	sessionId    = request.values.get('sessionId', None)
	callerNumber = request.values.get('callerNumber', None)

	if isActive == '1':
		callerNumber = request.values.get('callerNumber', None)
		logging.info('caller is {}'.format(callerNumber))

		response = '<Response>'
		response += '<Say maxDuration="60" playBeep="false"> Hi, '
		response += 'Welcome Mr </Say>'
		response += 'name="{}"'.format(name)
		response += '<Say> For inspiration messages on overcoming procrastination, Press 1'
		response += 'For messages on self-improvement, Press 2 </Say>'

		'''
		User has just been prompted to input key.
		Here will come in code to capture that input.
		Below is code that will act based on input.
		'''
		if input == 1:
			#i suppose the best way would be, have all the audio files
			#online somewhere, then here call them randomly based on selection(input) made.

			'''
			if selection is 1:
				play random audio file in that category
			elif selection is 2:
				play random audio file in that category
			elif selection is 3:
				play random audio file in that category
			'''
			


###to be continued