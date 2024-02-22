db=1
from flask import Flask, flash, redirect, render_template, request, session, abort
import pandas as pd
import random
import googlemaps
from datetime import datetime
from googlemaps import Client
from flask import jsonify

from flask_sqlalchemy import SQLAlchemy


df = pd.read_csv('Data/uscities.csv')
#print(df.shape)
df = df.drop(df[df['state_name'] == 'Hawaii'].index)
#print(df.shape)
df = df.drop(df[df['state_name'] == 'Alaska'].index)
df = df.drop(df[df['state_name'] == 'Puerto Rico'].index)
import simplejson#, urllib
import urllib.request


app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///leaderboard.db'

db = SQLAlchemy(app)


class leaderBoard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer, nullable=False)
    date_added = db.Column(db.DateTime,default =  datetime.utcnow)

    def __repr__(self):
        return '<score %r>' % self.score


app.secret_key = "abcde2o38cniuwc"

@app.route("/", methods = ['GET','POST'])
def index():
    
    '''if request.method == 'GET':
        session['cit1'] = random.randint(0,31119)
        session['cityOne'] = df["city"][session['cit1']]
        session['cit2'] = random.randint(0,31119)
        session['cityTwo'] = df["city"][session['cit2']]
        session['latOne'] = float(df["lat"][session['cit1']])
        session['lonOne'] = float(df["lng"][session['cit1']])
        session['latTwo'] = float(df["lat"][session['cit2']])
        session['lonTwo'] = float(df["lng"][session['cit2']])
        return render_template('index.html', cityOne = session['cityOne'] , cityTwo = session['cityTwo'], latOne =session['latOne'], latTwo=session['latTwo'],lonOne=session['lonOne'],lonTwo=session['lonTwo']  )
'''
    # session['cityOne'] = ""
    # session['cit1'] = ""
    # session['cityOne'] = ""
    # session['cit2'] = ""
    # session['cityTwo'] =""
    # session['latOne'] = ""
    # session['lonOne'] = ""
    # session['LeaderBoardData'] =""
    # session['latTwo'] = ""
    # session['lonTwo'] = ""
    return render_template('index.html', cityOne = session['cityOne'] , cityTwo = session['cityTwo'], latOne =session['latOne'], latTwo=session['latTwo'],lonOne=session['lonOne'],lonTwo=session['lonTwo']  )

    #return render_template('index.html')



@app.route('/create_file', methods=['POST','GET'])
def create_file():
    session['cit1'] = random.randint(0,31119)
    session['cityOne'] = df["city"][session['cit1']]
    session['cit2'] = random.randint(0,31119)
    session['cityTwo'] = df["city"][session['cit2']]
    session['latOne'] = float(df["lat"][session['cit1']])
    session['lonOne'] = float(df["lng"][session['cit1']])
    session['latTwo'] = float(df["lat"][session['cit2']])
    session['lonTwo'] = float(df["lng"][session['cit2']])
    return jsonify({"Location 2 Text" : "Location 2:" + session['cityTwo'],
                    "Location 1 Text": "Location 1:" + session['cityOne'],
                     "Location 2 Lat": session['latTwo'], 
                      "Location 2 Lon": session['lonTwo'],
                      "Location 1 Lat": session['latOne'],
                      "Location 1 Lon": session['lonOne']})
    if request.method == 'GET':
        
        return render_template('index.html', cityOne = session['cityOne'] , cityTwo = session['cityTwo'], latOne =session['latOne'], latTwo=session['latTwo'],lonOne=session['lonOne'],lonTwo=session['lonTwo']  )



@app.route("/submitGuess", methods = ['POST','GET'])
def submitGuess():
    session['key'] = "AIzaSyDF5OmFRJoUh2qk7KmI79Rk0Zdkcl4dbgM"
    gmaps = Client(key=session['key'])

    
    gmaps = googlemaps.Client(key=session['key'])

    #session['orig'] = str(session['latOne'])+", "+str(session['lonOne'])
    #session['dest'] = str(session['latTwo'])+", "+str(session['lonTwo'])
    session['orig'] = session['latOne'],session['lonOne']
    session['dest'] = session['latTwo'],session['lonTwo']

    #return session['orig']
    now = datetime.now()
    directions_result = gmaps.directions(session['orig'],
                                     session['dest'],
                                     mode="walking",
                                     departure_time=now
                                    )
    #return directions_result[0]['legs'][0]['distance']['text']
    #return directions_result[0]['legs'][0]['duration']['text']
    #print(directions_result[0]['legs'][0]['duration']['text'])
    #return directions_result[0]['legs'][0]['distance']['text']
   
    #print(cityOne)
    #return session['cityOne']
    
    #if directions_result[0]['legs'][0]['duration']['value'] == None:
     #   return "not possible to walk there,regenerate"
    
    #try:
    session['time'] = directions_result[0]['legs'][0]['duration']['value']
    #except ValueError:
     #   return "It is not possible to walk to one of the above cities, please generate again!"
    #return render_template('index.html', cityOne = session['cityOne'] , cityTwo = session['cityTwo'], latOne =session['latOne'], latTwo=session['latTwo'],lonOne=session['lonOne'],lonTwo=session['lonTwo'], time=session['time']  )
    #try:
    score = session['time'] - int(request.form['guess'])
    if score < 0:
        score = session['time']
    return jsonify({"time": "Correct Answer: " + str(session['time']) + " seconds",
                    "myScore": "Your Score: " + str(score) + " points!" })
    #return render_template('index.html',cityOne = cityOne , cityTwo = cityTwo)
    #except:
     #   raise Exception( "Please enter your ")
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

