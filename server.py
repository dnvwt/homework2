from flask import Flask, request, jsonify, Response
import dicttoxml
import xmltodict
import uuid
app = Flask(__name__)
@app.route("/to_xml/<req_id>", methods = ["POST"])
def to_xml(req_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON"}), 400
    data["request_id"] = req_id
    xml_data = dicttoxml.dicttoxml(data,custom_root='personal_data', attr_type = False)
    return Response(xml_data, mimetype='application/xml')
@app.route("/to_json/<req_id>", methods = ["POST"])
def to_json(req_id):
    xml_data = request.data()
    if not xml_data:
        return jsonify({"error": "No XML"}), 400
    dict_data = xmltodict.parse(xml_data)
    dict_data["request_id"] = req_id
    return jsonify(dict_data)
if __name__ == "__main__":
    app.run(port=5002, debug=True)