#perpose is to transport the info from the api file to frontend in a readable way and updating the frontend every minute
from google_maps_info import *
import schedule
import time
import argparse
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/get_google_maps_info')
def get_google_maps_info_endpoint():
    data = top_ten_restaurants_info()
    return jsonify(data)


if __name__ == '__main__':
    app.run()








