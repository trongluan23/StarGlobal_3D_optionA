from untils.openAI import client

def create(json_data):
    
    prompt = f"""Bạn là một chuyên gia trong lĩnh vực bất động sản, quản lý và tổ chức nội dung các dự án số hóa 3D.
    
    Input:
    + Tên dự án/không gian 3D: {json_data['name']}
    + Loại không gian (căn hộ, văn phòng, cửa hàng, triển lãm...): {json_data['loaiKG']}
    + Mô tả ngắn về nội dung/mục đích sử dụng: {json_data['moTa']}
    + Nhóm khách hàng mục tiêu: {json_data['nhomKH']}
    ** Tự tìm kiếm nhóm khách hàng phù hợp nếu {json_data['nhomKH']} là rỗng **
    
    Hãy trả về kết quả dưới dạng JSON với các trường sau:
    + tieu_de: Tiêu đề mô tả dự án chuẩn cho trang giới thiệu
    + mo_ta_ngan: Đoạn mô tả ngắn hấp dẫn cho khách hàng (tone phù hợp ngành BDS/bán lẻ/triển lãm)
    + diem_noi_bat: 3–5 điểm nổi bật của không gian (AI tự đề xuất dựa trên loại không gian)
    + goi_y_so_hoa: Gợi ý các điểm cần chú ý khi số hóa 3D loại không gian này
    """
    result = client.chat.completions.create(
        model="gpt-4o",
        response_format={"type": "json_object"},
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    content = result.choices[0].message.content
    return content

# if __name__ == "__main__":
#     json_data = {
#         'name': 'Vin home',
#         'loaiKG': 'căn hộ',
#         'moTa': 'Căn hộ dịch vụ 2 phòng ngủ đầy đủ tiện nghi, sang trọng',
#         'nhomKH': 'Gia đình'
#     }

#     print(create(json_data))