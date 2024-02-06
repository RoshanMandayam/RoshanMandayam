from flask import Flask, flash, redirect, render_template, request, session, abort
import pandas as pd
import random
import googlemaps
from datetime import datetime
from googlemaps import Client
from flask import jsonify

df = pd.read_csv('Data/uscities.csv')
print(df.shape)
df = df.drop(df[df['state_name'] == 'Hawaii'].index)
print(df.shape)

import simplejson#, urllib
import urllib.request


app = Flask(__name__)
app.secret_key = "abcde2o38cniuwc"
'''cityOne = ""
cityTwo = ""
latOne = 0
latTwo = 0
lonOne =0
lonTwo = 0
time = 0
'''
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
    return render_template('index.html', cityOne = session['cityOne'] , cityTwo = session['cityTwo'], latOne =session['latOne'], latTwo=session['latTwo'],lonOne=session['lonOne'],lonTwo=session['lonTwo']  )

    #return render_template('index.html')

'''@app.route("/generateLocOne")
def generateLocOne():
    cit1 = random.randint(0,31119)
    cityOne = df["city"][cit1]
    return render_template('index.html', cityOne =cityOne, cityTwo = cityTwo )

@app.route("/generateLocTwo")
def generateLocTwo():
    cit2 = random.randint(0,31119)
    cityTwo = df["city"][cit2]
    return render_template('index.html', cityOne = cityOne , cityTwo = cityTwo )
'''

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
    session['key'] = "AIzaSyASClaRoPWzq11Xo0cUQ1UpfJYtMd_XxoI"
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
    
    '''session['url'] = "https://maps.googleapis.com/maps/api/distancematrix/json?key={0}&origins={1}&destinations={2}&mode=driving&language=en-EN&sensor=false".format(session['key'],(session['orig']),(session['dest']))
    session['url'] = session['url'].replace("%20", "")
    session['url'] = session['url'].replace(" ", "")
    session['result']= simplejson.load(urllib.request.urlopen(session['url']))
    #return (session['url'])
    return session['result']['rows'][0]['elements'][0]
    session['time'] = session['result']['rows'][0]['elements'][0]['duration']['text']
    '''
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
        score = 0
    return jsonify({"time": "Correct Answer: " + str(session['time']) + " seconds",
                    "myScore": "Your Score: " + str(score) + " points!" })
    #return render_template('index.html',cityOne = cityOne , cityTwo = cityTwo)
    #except:
     #   raise Exception( "Please enter your ")
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)


