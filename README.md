# 🏢 Hệ thống Tạo Nội dung Dự án 3D tự động


## Cài đặt và chạy

### 1. Clone hoặc tải dự án về

### 2. Cài đặt thư viện Python

```bash
pip install -r requirements.txt
```

### 3. Cấu hình OpenAI API Key

Tạo file `.env` trong thư mục gốc dự án:

```env
OPENAI_API_KEY= "API key"
```
*** Nếu không có key OpenAI pro hãy đổi model gpt sang model gpt-4o-mini miễn phí trong file genContent.py


> Lấy API key tại: https://platform.openai.com/api-keys

### 4. Chạy ứng dụng

```bash
python app.py
```

Server sẽ khởi động tại: **http://localhost:5000**


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

