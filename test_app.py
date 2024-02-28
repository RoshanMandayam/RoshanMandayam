import unittest
from app import genLocations,app
import pytest
#from . import __version__ as _werkzeug_version
from flask import Flask,request
from flask import json
from werkzeug.test import Client
from werkzeug.testapp import test_app as te
# app = Flask(__name__)
#c = Client(te)


def test_index():
    
    response = app.test_client().get("/")
    #print (response.data)
    #assert b"Location 2" in ( response.data )
    # with app.test_request_context():
    #     test = genLocations()
        
    #     return request.get_json
    #     #assert (test['Location 2 Text'] == "L")
    assert b"<title>Are We There Yet?</title>" in response.data
    assert b"A single player map-based guessing game." in response.data

    #assert "It worked!"

def test_genLocations():
    response = app.test_client().get("/genLocations")
    assert response.status_code == 200
    assert "Location 2:" in response.json["Location 2 Text"] 


def test_submitGuess():
    #app.app_context().push()
    # with app.test_client() as c:
    #     with c.session_transaction() as sess:
    #         sess['latOne'] = '34'

    # once this is reached the session was stored
        #result = app.test_client().get('/submitGuess')
    response = app.test_client().post("/submitGuess", data={
         "guess": "643",
    })
    #assert result.status_code == 200                                
    assert response.status_code == 500