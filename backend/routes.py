from flask import Blueprint, jsonify
from backend.products import products

api = Blueprint('api', __name__)

@api.route('/api/products', methods=['GET'])
def get_products():
    print("GET /api/productsendpoint was hit")  
    return jsonify(products)

@api.route('/test', methods=['GET'])
def test():
    return "Test route is working"
