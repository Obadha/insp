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