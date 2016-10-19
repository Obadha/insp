'''
This is a standard file that stores information on a call i.e sessionId, callCost in a db
'''
import os
import sys

from app import db


class Voice(db.Model):
    __tablename__ = 'voice'

    sessionId = db.Column(db.String(250), primary_key = True)
    #no idea what this url leads to. Perhaps to voice file?
    url       = db.Column(db.String(250), nullable = False)
    callCost  = db.Column(db.Numeric(10), nullable = True)
    #i don't know what stt is
    stt       = db.Column(db.Text, nullable = True)

    def __repr__(self):
        return '<ID %r>' % self.sessionId