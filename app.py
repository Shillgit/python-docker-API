from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    """Health check endpoint"""
    return jsonify({
        'status': 'success',
        'message': 'Python Flask API is running!',
        'version': '1.0.0'
    })

@app.route('/api/health')
def health():
    """Detailed health check"""
    return jsonify({
        'status': 'healthy',
        'service': 'python-api',
        'environment': os.getenv('ENVIRONMENT', 'development')
    })

@app.route('/api/data')
def get_data():
    """Sample data endpoint"""
    return jsonify({
        'data': [
            {'id': 1, 'name': 'Item One', 'value': 100},
            {'id': 2, 'name': 'Item Two', 'value': 200},
            {'id': 3, 'name': 'Item Three', 'value': 300}
        ]
    })

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('DEBUG', 'False') == 'True'
    app.run(host='0.0.0.0', port=port, debug=debug)
