from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/", methods=['GET'])
def home():
    result = {'status': 'success'}
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True, threaded=True)
