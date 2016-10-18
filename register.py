'''
This file will read in content from sms sent by user. The contents of the sms will then be stored in the db table called
contacts.
From here, the user will then be directed on the next steps(what number to call) after registration is successful.
'''
import os
from app import (app, logging, db, settings)
from flask import (request, make_response)
from africastalking.AfricasTalkingGateway import (AfricasTalkingGateway, AfricasTalkingGatewayException)

from models.contacts import Contacts

@app.route('/sms', methods=['POST'])
def sms():
	_from = request.values.get('from',None) #from means the person from whom the text is coming from.
	text = request.values.get('text',None) #this gets the text in the message sent by user

	split_text = text.split('*')

	name   = split_text[0].capitalize()
	age    = split_text[1]
	gender = split_text[2].lower()


	count = Contacts.query.filter_by(phoneNumber = _from).count()

	if not count > 0:
		#no idea what api key is, what it does. Also, the use of the username is a mystery.
		gateway = AfricasTalkingGateway(os.environ.get('username'), os.environ.get('apikey')) 
		gateway.sendMessage (_from, "Thank you for registering for this service. To get inspiration messages, call 20880. Calls charged at 10 bob per minute. Have a blessed day.")

		#here the details are added to db table contacts
		contacts = Contacts (name=name, age = age, phoneNumber = _from)
		db.session.add(contacts)
		db.session.commit()
		logging.info("user added{}".format(contacts))

	else:
		logging.info("User already registered.")

	resp = make_response ("OK", 200)
	return resp