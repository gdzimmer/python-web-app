
from flask import Flask
from routes import initialize_routes

from flask_cors import CORS

app = Flask(__name__)

app.config['secret_key'] = 'Hello from the secret world of Flask!'
app.config['CORS_HEADERS'] = ['Content-Type','Authorization']
CORS(app, supports_credentials=True, resources={r"/api/*": {"origins": "*"}})

initialize_routes(app)

if __name__ == "__main__":
    app.run(debug=True)

# @app.route('/')
# def index():
#     return 'Hello World'
#
# def db():
#     return 'Hello DB Grads'
#
# app.add_url_rule('/api/db/', 'db', db)
