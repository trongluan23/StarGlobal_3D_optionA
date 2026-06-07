# 🏢 Hệ thống Tạo Nội dung Dự án 3D tự động

Ứng dụng web sử dụng AI (OpenAI GPT-4) để tự động tạo nội dung chuyên nghiệp cho các dự án số hóa không gian 3D trong lĩnh vực bất động sản, văn phòng, cửa hàng và triển lãm.

## ✨ Tính năng

- 🤖 **Tạo nội dung tự động**: Sử dụng GPT-4 để tạo mô tả dự án chuyên nghiệp
- 📝 **Form nhập liệu thông minh**: Giao diện trực quan, dễ sử dụng
- 🎨 **Kết quả được format đẹp**: Hiển thị rõ ràng, chuyên nghiệp
- 📋 **Copy nhanh**: Sao chép kết quả vào clipboard chỉ với 1 click
- 📱 **Responsive design**: Hoạt động tốt trên mọi thiết bị
- ⚡ **API RESTful**: Kiến trúc module hóa, dễ mở rộng

## 🛠️ Công nghệ sử dụng

**Backend:**
- Flask 3.0 - Web framework
- OpenAI API (GPT-4) - AI content generation
- Flask-CORS - Cross-origin resource sharing
- Python-dotenv - Environment variable management

**Frontend:**
- HTML5 + CSS3
- JavaScript (Vanilla)
- Bootstrap 5 - UI framework

## 📋 Yêu cầu hệ thống

- Python 3.8+
- OpenAI API key
- Trình duyệt web hiện đại (Chrome, Firefox, Safari, Edge)

## 🚀 Cài đặt và chạy

### 1. Clone hoặc tải dự án về


### 2. Cài đặt thư viện Python

```bash
pip install -r requirements.txt
```

### 3. Cấu hình OpenAI API Key

Tạo file `.env` trong thư mục gốc dự án:

```env
OPENAI_API_KEY=sk-your-api-key-here
```

> 💡 Lấy API key tại: https://platform.openai.com/api-keys

### 4. Chạy ứng dụng

```bash
python app.py
```

Server sẽ khởi động tại: **http://localhost:5000**


Nếu có vấn đề hoặc góp ý, vui lòng tạo issue hoặc liên hệ team phát triển.

---

**Made with ❤️ using Flask & OpenAI GPT-4**
