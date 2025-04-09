from flask import Blueprint, jsonify
from backend.products import products

api = Blueprint('api', __name__)

@api.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)