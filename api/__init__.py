from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from untils.openAI import client
import json
import os

from untils.genContent import create

def create_app():
    # Get the parent directory (project root)
    template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
    static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))
    
    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
    CORS(app) 
    
    
    
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/api/generate', methods=['POST'])
    def generate_content():
        try:
            data = request.get_json()
            
            print(data)
            
            result = create(data)
            result_json = json.loads(result)
            
            return jsonify(result_json)
            
        except Exception as e:
            # Handle errors
            print(f"Error: {str(e)}")
            return jsonify({
                "error": str(e),
                "message": "Có lỗi xảy ra khi tạo nội dung"
            }), 500
    
    return app

