from flask import Flask
from flask_cors import CORS
from backend.routes import api

app = Flask(__name__)
CORS(app)  # allow cross-origin requests (from React)

app.register_blueprint(api, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
