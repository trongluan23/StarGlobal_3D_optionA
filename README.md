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

## 📁 Cấu trúc dự án

```
TEST/
├── api/
│   └── __init__.py         # Flask app factory & routes
├── untils/
│   ├── openAI.py          # OpenAI client configuration
│   └── genContent.py      # Content generation logic
├── static/
│   └── app.js             # Frontend JavaScript
├── templates/
│   └── index.html         # Giao diện HTML chính
├── app.py                 # Entry point
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (không commit)
└── README.md             # Documentation
```

## 📖 Hướng dẫn sử dụng

### 1. Truy cập giao diện web

Mở trình duyệt và truy cập: `http://localhost:5000`

### 2. Nhập thông tin dự án

Điền vào form với các thông tin:
- **Tên dự án/không gian 3D**: VD: "Căn hộ Vinhomes Ocean Park"
- **Loại không gian**: VD: "Căn hộ cao cấp", "Văn phòng", "Showroom"
- **Mô tả ngắn**: Mô tả mục đích sử dụng và đặc điểm
- **Nhóm khách hàng**: VD: "Gia đình trẻ", "Doanh nghiệp", "Nhà đầu tư"

### 3. Tạo nội dung

Nhấn nút **"Tạo Nội dung"** và chờ AI xử lý (3-5 giây)

### 4. Nhận kết quả

Hệ thống sẽ trả về:
- ✅ **Tiêu đề dự án**: Tiêu đề hấp dẫn, chuẩn SEO
- ✅ **Mô tả ngắn**: Đoạn giới thiệu thu hút khách hàng
- ✅ **3-5 điểm nổi bật**: Các ưu điểm chính của không gian
- ✅ **Gợi ý số hóa 3D**: Các điểm cần chú ý khi chụp/quay 3D

### 5. Sử dụng kết quả

- Nhấn **"Sao chép"** để copy toàn bộ vào clipboard
- Nhấn **"Tạo mới"** để làm dự án khác

## 🔌 API Endpoints

### `GET /`
Trả về giao diện web chính

### `POST /api/generate`
Tạo nội dung dự án từ thông tin đầu vào

**Request Body:**
```json
{
  "name": "Căn hộ Vinhomes Ocean Park",
  "loaiKG": "Căn hộ cao cấp",
  "moTa": "Căn hộ 2 phòng ngủ view biển, đầy đủ nội thất",
  "nhomKH": "Gia đình trẻ"
}
```

**Response:**
```json
{
  "tieu_de": "...",
  "mo_ta_ngan": "...",
  "diem_noi_bat": ["...", "...", "..."],
  "goi_y_so_hoa": ["...", "...", "..."]
}
```

## 🔧 Development

### Chạy ở chế độ debug

File `app.py` đã được cấu hình sẵn `debug=True`, tự động reload khi có thay đổi code.

### Thêm tính năng mới

1. **Backend**: Chỉnh sửa `api/__init__.py` để thêm routes
2. **AI Logic**: Chỉnh sửa `untils/genContent.py` để tùy chỉnh prompt
3. **Frontend**: Chỉnh sửa `static/app.js` và `templates/index.html`

## 🐛 Xử lý lỗi thường gặp

### Lỗi: `Template not found`
- **Nguyên nhân**: Flask không tìm thấy thư mục templates
- **Giải pháp**: Đã được fix trong `api/__init__.py` với `template_folder` và `static_folder`

### Lỗi: `OPENAI_API_KEY not found`
- **Nguyên nhân**: Chưa tạo file `.env` hoặc API key sai
- **Giải pháp**: Kiểm tra file `.env` có tồn tại và đúng format

### Lỗi: `The view function did not return a valid response`
- **Nguyên nhân**: Function không có `return` statement
- **Giải pháp**: Đã được fix, tất cả routes đều có return hợp lệ

### Lỗi: `Rate limit exceeded`
- **Nguyên nhân**: Gọi API quá nhiều/nhanh
- **Giải pháp**: Chờ 1 phút hoặc nâng cấp plan OpenAI

## 📝 TODO / Roadmap

- [ ] Thêm history lưu các lần tạo nội dung
- [ ] Export kết quả ra file Word/PDF
- [ ] Hỗ trợ nhiều ngôn ngữ (EN, VN)
- [ ] Tích hợp database để lưu projects
- [ ] Thêm template có sẵn cho từng loại không gian
- [ ] Upload hình ảnh để AI phân tích và tạo nội dung

## 📄 License

This project is for internal use.

## 👤 Liên hệ

Nếu có vấn đề hoặc góp ý, vui lòng tạo issue hoặc liên hệ team phát triển.

---

**Made with ❤️ using Flask & OpenAI GPT-4**
