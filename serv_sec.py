from flask import Flask, jsonify, request
import requests
app = Flask(__name__)
SERVER_URL = "http://127.0.0.1:5001/save"
@app.route('/send', methods = ["POST"])
def proxy():
    data = request.get_json()
    if not data:
        return jsonify({"status": "error", "message": "no JSON recieved"}), 400
    response = requests.post(SERVER_URL, json=data)
    return jsonify(response.json())
if __name__ == '__main__':
    app.run(port=5000, debug=True)

