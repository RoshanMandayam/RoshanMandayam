import googlemaps
from datetime import datetime
from googlemaps import Client

def calc_seconds(orig,dest):
    keyG = "AIzaSyDF5OmFRJoUh2qk7KmI79Rk0Zdkcl4dbgM"
    gmaps = Client(key=keyG)

    
    gmaps = googlemaps.Client(key=keyG)


    now = datetime.now()
    directions_result = gmaps.directions(orig,
                                     dest,
                                     mode="walking",
                                     departure_time=now
                                    )
 

    time = directions_result[0]['legs'][0]['duration']['value']

    return time