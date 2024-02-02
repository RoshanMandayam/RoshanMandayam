from flask import Flask, flash, redirect, render_template, request, session, abort
import pandas as pd
import random
import googlemaps
from datetime import datetime
from googlemaps import Client

df = pd.read_csv('Data/uscities.csv')


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
@app.route("/")
def index():
    return render_template('index.html')

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
@app.route("/generateLocations")
def generateLocations():
    #session['cityOne'] = "blah"
    session['cit1'] = random.randint(0,31119)
    session['cityOne'] = df["city"][session['cit1']]
    session['cit2'] = random.randint(0,31119)
    session['cityTwo'] = df["city"][session['cit2']]
    session['latOne'] = float(df["lat"][session['cit1']])
    session['lonOne'] = float(df["lng"][session['cit1']])
    session['latTwo'] = float(df["lat"][session['cit2']])
    session['lonTwo'] = float(df["lng"][session['cit2']])

    return render_template('index.html', cityOne = session['cityOne'] , cityTwo = session['cityTwo'], latOne =session['latOne'], latTwo=session['latTwo'],lonOne=session['lonOne'],lonTwo=session['lonTwo']  )
  

@app.route("/submitGuess")
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
    print(directions_result[0]['legs'][0]['duration']['text'])
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
    session['time'] = directions_result[0]['legs'][0]['duration']['value']
    return render_template('index.html', cityOne = session['cityOne'] , cityTwo = session['cityTwo'], latOne =session['latOne'], latTwo=session['latTwo'],lonOne=session['lonOne'],lonTwo=session['lonTwo'], time=session['time']  )
    
    #return render_template('index.html',cityOne = cityOne , cityTwo = cityTwo)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)


'''
https://maps.googleapis.com/maps/api/distancematrix/json?key={0}&origins={1}&destinations={2}&mode=driving&language=en-EN&sensor=false".format(key,(session['orig']),str(session['dest']))

https://maps.googleapis.com/maps/api/distancematrix/json?key=AIzaSyASClaRoPWzq11Xo0cUQ1UpfJYtMd_XxoI&origins=(34.9776,-91.5067)&destinations=(41.2128,-75.8993)&mode=driving&language=en-EN&sensor=false



"https://maps.googleapis.com/maps/api/distancematrix/json?key=AIzaSyASClaRoPWzq11Xo0cUQ1UpfJYtMd_XxoI&origins=(34.9776,-91.5067)&destinations=(41.2128,-75.8993)&mode=driving&language=en-EN&sensor=false"


'''