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
		callerNumber = request.values.get('callerNumber', None) #gets the number of caller
		logging.info("caller is {}".format(callerNumber)) #logs number of caller

		response = '<Response>' #Beginning of audio response that will be played out.
		response += '<Say maxDuration="60" playBeep="false"> Welcome, Mr </Say>'
		response += 'name="{}"'.format(name)
		response += '<Play url ="link-to-audio-file">' #this will be picking a random audio file

		
		
		response += "</Response>"

		voice = Voice.(sessionId=sessionId,url='')
		db.session.add(voice)
		db.session.commit()

	else:
		voice = Voice.query.filter_by(sessionId = sessionId).first()
		voice.callCost = request.values.get('amount', None)

		db.session.add(voice)
		db.session.commit()
		logging.info(request.values)

		response = ""

	resp = make_response(response, 200)
	resp.headers['Content-Type'] = "application/xml"
	return resp


###to be continued