from flask import Flask
from flask import request
import requests

app = Flask(__name__)

@app.route('/pipeline', methods=['PUT', 'GET'])
def pipeline():
    if request.method == 'GET':
        return {"pipeline": "Started"}
    if request.method == 'PUT':
        r = requests.put("http://localhost:5001/pipeline", json={'pipeline': 'start'})
        return r.json()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)