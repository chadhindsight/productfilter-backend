from flask import Flask
from flask_cors import CORS
from backend.routes import api

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})  # CORS for /api/* explicitly

app.register_blueprint(api)

if __name__ == '__main__':
    app.run(debug=True)

