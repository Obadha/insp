'''
Here we save user info when they register by sms
'''
from app import db

class Contacts(db.Model):

	__tablename__ = 'members'

	phoneNumber = db.Column(db.String(20),primary_key=True) #this is captured automatically
	name = db.Column(db.String(50), nullable = False)
	age = db.Column(db.String(10), nullable = False)
	gender = db.Column(db.String(20), nullable = False)

	def __repr__ (self):
		#from this we will get the name to address them with in the call.
		return '<name %r>' % self.name
