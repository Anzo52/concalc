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
from flask_cors import CORS
import json
import requests
import sys
import os
import math


app = Flask(__name__)

def inches_to_yards(inches):
    return inches / 36

def feet_to_yards(feet):
    return feet / 3


def get_curb_gutter_volume(base_width_inches, toe_height_inches, face_height_inches, curb_width_inches, length_feet):
    base_width_yards = inches_to_yards(base_width_inches)
    toe_height_yards = inches_to_yards(toe_height_inches)
    face_height_yards = inches_to_yards(face_height_inches)
    curb_width_yards = inches_to_yards(curb_width_inches)
    length_yards = feet_to_yards(length_feet)

    volume_cubic_yards = (base_width_yards * toe_height_yards * length_yards) + (curb_width_yards * face_height_yards * length_yards)
    return volume_cubic_yards


def get_sidewalk_volume(thickness_inches, width_feet, length_feet):
    thickness_yards = inches_to_yards(thickness_inches)
    width_yards = feet_to_yards(width_feet)
    length_yards = feet_to_yards(length_feet)

    volume_cubic_yards = thickness_yards * width_yards * length_yards
    return volume_cubic_yards


def get_patio_volume(thickness_inches, width_feet, length_feet):
    thickness_yards = inches_to_yards(thickness_inches)
    width_yards = feet_to_yards(width_feet)
    length_yards = feet_to_yards(length_feet)

    volume_cubic_yards = thickness_yards * width_yards * length_yards
    return volume_cubic_yards


@app.route('/concalc/test/curbgutter', methods=['GET'])
def test_curb_gutter():
    base_width_inches = request.args.get('base_width_inches', type=int)
    toe_height_inches = request.args.get('toe_height_inches', type=int)
    face_height_inches = request.args.get('face_height_inches', type=int)
    curb_width_inches = request.args.get('curb_width_inches', type=int)
    length_feet = request.args.get('length_feet', type=int)

    volume_cubic_yards = get_curb_gutter_volume(base_width_inches, toe_height_inches, face_height_inches, curb_width_inches, length_feet)
    return jsonify(volume_cubic_yards=volume_cubic_yards)


@app.route('/concalc/test/sidewalk', methods=['GET'])
def test_sidewalk():
    thickness_inches = request.args.get('thickness_inches', type=int)
    width_feet = request.args.get('width_feet', type=int)
    length_feet = request.args.get('length_feet', type=int)

    volume_cubic_yards = get_sidewalk_volume(thickness_inches, width_feet, length_feet)
    return jsonify(volume_cubic_yards=volume_cubic_yards)


@app.route('/concalc/test/patio', methods=['GET'])
def test_patio():
    thickness_inches = request.args.get('thickness_inches', type=int)
    width_feet = request.args.get('width_feet', type=int)
    length_feet = request.args.get('length_feet', type=int)

    volume_cubic_yards = get_patio_volume(thickness_inches, width_feet, length_feet)
    return jsonify(volume_cubic_yards=volume_cubic_yards)


@app.route('/concalc/api/v1/curbgutter', methods=['GET'])
def curb_gutter():
    base_width_inches = request.args.get('base_width_inches', type=int)
    toe_height_inches = request.args.get('toe_height_inches', type=int)
    face_height_inches = request.args.get('face_height_inches', type=int)
    curb_width_inches = request.args.get('curb_width_inches', type=int)
    length_feet = request.args.get('length_feet', type=int)

    volume_cubic_yards = get_curb_gutter_volume(base_width_inches, toe_height_inches, face_height_inches, curb_width_inches, length_feet)
    return jsonify(volume_cubic_yards=volume_cubic_yards)


@app.route('/concalc/api/v1/sidewalk', methods=['GET'])
def sidewalk():
    thickness_inches = request.args.get('thickness_inches', type=int)
    width_feet = request.args.get('width_feet', type=int)
    length_feet = request.args.get('length_feet', type=int)

    volume_cubic_yards = get_sidewalk_volume(thickness_inches, width_feet, length_feet)
    return jsonify(volume_cubic_yards=volume_cubic_yards)


@app.route('/concalc/api/v1/patio', methods=['GET'])
def patio():
    thickness_inches = request.args.get('thickness_inches', type=int)
    width_feet = request.args.get('width_feet', type=int)
    length_feet = request.args.get('length_feet', type=int)

    volume_cubic_yards = get_patio_volume(thickness_inches, width_feet, length_feet)
    return jsonify(volume_cubic_yards=volume_cubic_yards)


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='


# curl -X GET "http://localhost:5000/concalc/api/v1/curbgutter?base_width_inches=12&toe_height_inches=12&face_height_inches=12&curb_width_inches=12&length_feet=12"
# curl -X GET "http://localhost:5000/concalc/api/v1/sidewalk?thickness_inches=12&width_feet=12&length_feet=12"
