from flask import Flask, jsonify
from src.routes.users import users_bp
import os

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({"status": "up", "db": "mysql"}), 200

app.register_blueprint(users_bp, url_prefix='/api/v1/users')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)