from flask import jsonify
from App import app
from Logger import log

@app.route('/log', methods=['GET'])
def get_log():
    return jsonify({'log': log}), 200
