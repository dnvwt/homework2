from flask import Flask, request, jsonify
app = Flask(__name__)
database=[]
@app.route('/save', methods = ['POST'])
def save_data():
    data = request.get_json()
    if not data:
        return jsonify({"status": "error", "message": "no JSON recieved"}), 400
    database.append(data)
    print("now:", database)
    return jsonify({"status": "ok", "saved": data}), 200
if __name__ == '__main__':
    app.run(port=5001, debug=True)