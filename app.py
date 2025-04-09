# from flask import Flask
# from flask_cors import CORS
# from backend.routes import api

# app = Flask(__name__)
# CORS(app) 

# app.register_blueprint(api, url_prefix='/api')  # Register blueprint with URL prefix

# # Test route for validation
# @app.route('/test')
# def test():
#     return "Test route is working!"

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask
from flask_cors import CORS
from backend.routes import api

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})  # CORS for /api/* explicitly

app.register_blueprint(api)

if __name__ == '__main__':
    app.run(debug=True)

