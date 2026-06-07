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
            name = data.get('name', '')
            loaiKG = data.get('loaiKG', '')
            moTa = data.get('moTa', '')
            nhomKH = data.get('nhomKH', '')
            
            print(data)
            
    #         prompt = f"""Bạn là một chuyên gia trong lĩnh vực bất động sản, quản lý và tổ chức nội dung các dự án số hóa 3D.

    # Input:
    # + Tên dự án/không gian 3D: {name}
    # + Loại không gian (căn hộ, văn phòng, cửa hàng, triển lãm...): {loaiKG}
    # + Mô tả ngắn về nội dung/mục đích sử dụng: {moTa}
    # + Nhóm khách hàng mục tiêu: {nhomKH}

    # Hãy trả về kết quả dưới dạng JSON với các trường sau:
    # + tieu_de: Tiêu đề mô tả dự án chuẩn cho trang giới thiệu
    # + mo_ta_ngan: Đoạn mô tả ngắn hấp dẫn cho khách hàng (tone phù hợp ngành BDS/bán lẻ/triển lãm)
    # + diem_noi_bat: 3–5 điểm nổi bật của không gian (AI tự đề xuất dựa trên loại không gian) - trả về dạng mảng
    # + goi_y_so_hoa: Gợi ý các điểm cần chú ý khi số hóa 3D loại không gian này - trả về dạng mảng
    # """
            
    #         # Gọi OpenAI API
    #         response = client.chat.completions.create(
    #             model="gpt-4o",
    #             response_format={"type": "json_object"},
    #             messages=[
    #                 {"role": "user", "content": prompt}
    #             ]
    #         )
            
    #         # Parse kết quả
    #         result_text = response.choices[0].message.content
            result = create(data)
            result_json = json.loads(result)
            
            return jsonify(result_json)
            
        except Exception as e:
            print(f"Error: {str(e)}")
            return jsonify({
                "error": str(e),
                "message": "Có lỗi xảy ra khi tạo nội dung"
            }), 500
    
    return app

