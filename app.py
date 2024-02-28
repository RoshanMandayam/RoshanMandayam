from flask import Flask, flash, redirect, render_template, request, session, abort
import pandas as pd
import random
import googlemaps
from datetime import datetime
from googlemaps import Client
from flask import jsonify

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from gmaps_api import calc_seconds

df = pd.read_csv('data/uscities.csv')
#print(df.shape)
df = df.drop(df[df['state_name'] == 'Hawaii'].index)
#print(df.shape)
df = df.drop(df[df['state_name'] == 'Alaska'].index)
df = df.drop(df[df['state_name'] == 'Puerto Rico'].index)
import simplejson#, urllib
import urllib.request


app = Flask(__name__)
ma = Marshmallow(app)
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
    session['LeaderBoardData'] = ''
    session['cityOne'] = ''
    session['cityTwo'] = ''
    session['latOne'] =''
    session['latTwo']=''
    session['lonOne']=''
    session['lonTwo']=''
    return render_template('index.html', position = session['LeaderBoardData'], cityOne = session['cityOne'] , cityTwo = session['cityTwo'], latOne =session['latOne'], latTwo=session['latTwo'],lonOne=session['lonOne'],lonTwo=session['lonTwo']  )


@app.route('/genLocations', methods=['POST','GET'])
def genLocations():
    session['LeaderBoardData'] = ''
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


@app.route("/submitGuess", methods = ['POST','GET'])
def submitGuess():
    session['orig'] = session['latOne'],session['lonOne']
    session['dest'] = session['latTwo'],session['lonTwo']


    session['time'] = calc_seconds(session['orig'],session['dest'])
    score = session['time'] - int(request.form['guess'])
    if score < 0:
        score = session['time']

    attempt = leaderBoard(score = score)
    db.session.add(attempt)
    db.session.commit()
    board = leaderBoard.query.order_by(leaderBoard.score).limit(10)
    #board = jsonify(board)
    #session['LeaderBoardData'] = leaderBoard.query.order_by(leaderBoard.date_added)
    return jsonify({"time": "Correct Answer: " + str(session['time']) + " seconds",
                    "myScore": "Your Score: " + str(score) + " points!", "data": [{ "id": str(user.id) + " ;  " , "score": str(user.score) + " points ", "date":str(user.date_added) + " ; "} for user in board] }
                    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)


