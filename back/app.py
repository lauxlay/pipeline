from flask import Flask
from flask import request
import requests
import time

app = Flask(__name__)

@app.route('/pipeline', methods=['PUT', 'GET'])
def pipeline():
    if request.method == 'GET':
        return {"pipeline": "Started"}
    if request.method == 'PUT':
        data = request.json
        time.sleep(30)
        if data == {'pipeline': 'start'}:
            return {"pipeline": "started"}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)