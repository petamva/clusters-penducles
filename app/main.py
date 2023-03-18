import base64
from io import BytesIO
from PIL import Image
from flask import Flask, jsonify, request
from flask_cors import CORS
import app.utils.utils as utils


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
# app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)


@app.route('/')
def index():
    return 'Welcome!'


@app.route('/clusters', methods=['GET', 'POST'])
def predict_cluster():
    up_file = request.files['file']
    read_file = up_file.read()
    image = Image.open(BytesIO(read_file))
    prediction_bytes = utils.make_prediction(image, service='clusters')
    img_bytes = base64.b64encode(prediction_bytes)
    return jsonify({'image': f'{img_bytes}'})



@app.route('/penducles', methods=['GET', 'POST'])
def predict_penducle():
    up_file = request.files['file']
    read_file = up_file.read()
    image = Image.open(BytesIO(read_file))
    prediction_bytes = utils.make_prediction(image, service='penducles')
    img_bytes = base64.b64encode(prediction_bytes)
    return jsonify({'image': f'{img_bytes}'})


if __name__ == "__main__":
    # Only for debugging while developing
    # app.run(host='0.0.0.0', debug=True, port=80)
    app.run(debug=True)
