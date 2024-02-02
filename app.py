from flask import Flask, flash, redirect, render_template, request, session, abort
import pandas as pd
import random
df = pd.read_csv('Data/uscities.csv')

app = Flask(__name__)
cityOne = ""
cityTwo = ""
latOne = 0
latTwo = 0
lonOne =0
lonTwo = 0
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
    cit1 = random.randint(0,31119)
    cityOne = df["city"][cit1]
    cit2 = random.randint(0,31119)
    cityTwo = df["city"][cit2]
    latOne = float(df["lat"][cit1])
    lonOne = float(df["lng"][cit1])
    latTwo = float(df["lat"][cit2])
    lonTwo = float(df["lng"][cit2])

    return render_template('index.html', cityOne = cityOne , cityTwo = cityTwo, latOne =latOne, latTwo=latTwo,lonOne=lonOne,lonTwo=lonTwo  )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)