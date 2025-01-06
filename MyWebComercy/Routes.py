from flask import request, jsonify
from ProductServices import AddProductService
from App import app

@app.route('/product/add', methods=['POST'])
def add_item():
    data = request.json
    [response, code] = AddProductService(data)
    return jsonify(response), code

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'UP'}), 200
