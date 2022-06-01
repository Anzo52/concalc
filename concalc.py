# Flask API for calculating volume of concrete needed to fill a given space.
# Endpoints and usage:
#   concalc/api/v1/curbgutter/<int:base_width_inches>&<int:toe_height_inches>&<int:face_height_inches>&<curb_width_inches>&<back_height_inches>&<length_feet>
#   concalc/api/v1/sidewalk/<int:thickness_inches>&<width_feet>&<length_feet>
#   concalc/api/v1/patio/<int:thickness_inches>&<width_feet>&<length_feet>
#
# Returns JSON object with the following fields:
#  double: volume_cubic_yards
#
# Documentation generated using flask-autodoc:
#   http://flask-autodoc.readthedocs.io/en/latest/



from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_cors import CORS
import json
import requests
import sys
import os
import math


app = Flask(__name__)
from flask_autodoc import Autodoc

auto = Autodoc(app)

api = Api(app)

def inches_to_yards(inches):
    return inches / 36

def feet_to_yards(feet):
    return feet / 3

class curbGutter(Resource):
    def get(self):
        # Get the base width, toe height, face height, curb width, and back height
        base_width_inches = request.args.get('base_width_inches')
        toe_height_inches = request.args.get('toe_height_inches')
        face_height_inches = request.args.get('face_height_inches')
        curb_width_inches = request.args.get('curb_width_inches')
        back_height_inches = request.args.get('back_height_inches')
        length_feet = request.args.get('length_feet')

        # Calculate the volume of concrete needed to fill the curb gutter
        base_width_yards = inches_to_yards(base_width_inches)
        toe_height_yards = inches_to_yards(toe_height_inches)
        face_height_yards = inches_to_yards(face_height_inches)
        curb_width_yards = inches_to_yards(curb_width_inches)
        back_height_yards = inches_to_yards(back_height_inches)
        length_yards = feet_to_yards(length_feet)
        vol_cubic_yards = (base_width_yards * toe_height_yards * face_height_yards * curb_width_yards * back_height_yards * length_yards)

        # Return the volume of concrete needed to fill the curb gutter
        return jsonify({'volume_cubic_yards': vol_cubic_yards})


class sidewalk(Resource):
    def get(self):
        # Get the thickness and width of the sidewalk
        thickness_inches = request.args.get('thickness_inches')
        width_feet = request.args.get('width_feet')
        length_feet = request.args.get('length_feet')

        # Calculate the volume of concrete needed to fill the sidewalk
        thickness_yards = inches_to_yards(thickness_inches)
        width_yards = feet_to_yards(width_feet)
        length_yards = feet_to_yards(length_feet)
        vol_cubic_yards = (thickness_yards * width_yards * length_yards)

        # Return the volume of concrete needed to fill the sidewalk
        return jsonify({'volume_cubic_yards': vol_cubic_yards})


class patio(Resource):
    def get(self):
        # Get the thickness and width of the patio
        thickness_inches = request.args.get('thickness_inches')
        width_feet = request.args.get('width_feet')
        length_feet = request.args.get('length_feet')

        # Calculate the volume of concrete needed to fill the patio
        thickness_yards = inches_to_yards(thickness_inches)
        width_yards = feet_to_yards(width_feet)
        length_yards = feet_to_yards(length_feet)
        vol_cubic_yards = (thickness_yards * width_yards * length_yards)

        # Return the volume of concrete needed to fill the patio
        return jsonify({'volume_cubic_yards': vol_cubic_yards})


api.add_resource(curbGutter, '/concalc/api/v1/curbgutter/<int:base_width_inches>&<int:toe_height_inches>&<int:face_height_inches>&<curb_width_inches>&<back_height_inches>&<length_feet>')
api.add_resource(sidewalk, '/concalc/api/v1/sidewalk/<int:thickness_inches>&<width_feet>&<length_feet>')
api.add_resource(patio, '/concalc/api/v1/patio/<int:thickness_inches>&<width_feet>&<length_feet>')


if __name__ == '__main__':
    app.run(debug=True)


# End of concalc.py