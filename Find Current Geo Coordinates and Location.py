# Find Current Geo Coordinates and Location.py
import geocoder

def get_location():
    g = geocoder.ip('me')
    return g.latlng, g.address