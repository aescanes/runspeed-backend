from flask import Flask, request
from flask_cors import CORS
from classes.speed import SpeedConverted

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/v1.0/pace-to-speed/<string:pace>', methods=['GET'])
def get_speed(pace: str) -> dict:
    """ get speed method """
    try:  
        s = SpeedConverted()
        return s.get_speed_from_pace(pace)
    except ValueError:
        return {'error': 'Only string values with format m:s'}

@app.route('/api/v1.0/speed-to-pace/<string:speed>', methods=['GET'])
def get_pace(speed: str) -> dict:
    try:
        s = SpeedConverted()
        return s.get_pace_from_speed(speed)
    except ValueError:
        return {'error': 'Only float values'}

if __name__ == '__main__':
    app.run(debug=True)