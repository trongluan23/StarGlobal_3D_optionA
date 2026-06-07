
document.getElementById('projectForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    
    const formData = {
        name: document.getElementById('projectName').value,
        loaiKG: document.getElementById('spaceType').value,
        moTa: document.getElementById('description').value,
        nhomKH: document.getElementById('targetCustomer').value
    };
    

    document.getElementById('loadingSpinner').classList.add('show');
    document.getElementById('resultSection').classList.remove('show');
    
    try {
        
        const response = await fetch('/api/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        });
        
        if (!response.ok) {
            throw new Error('Có lỗi xảy ra khi tạo nội dung');
        }
        
        const result = await response.json();
        displayResults(result);
        
    } catch (error) {
        console.error('Error:', error);
        alert('Có lỗi xảy ra: ' + error.message);
    } finally {
        document.getElementById('loadingSpinner').classList.remove('show');
    }
});

function displayResults(data) {
    
    document.getElementById('resultTitle').textContent = data.tieu_de || data.title || '';
    

    document.getElementById('resultDescription').textContent = data.mo_ta_ngan || data.description || '';
    

    const highlightsList = document.getElementById('resultHighlights');
    highlightsList.innerHTML = '';
    const highlights = data.diem_noi_bat || data.highlights || [];
    highlights.forEach(item => {
        const li = document.createElement('li');
        li.textContent = item;
        li.className = 'mb-2';
        highlightsList.appendChild(li);
    });
    

    const suggestionsList = document.getElementById('resultSuggestions');
    suggestionsList.innerHTML = '';
    const suggestions = data.goi_y_so_hoa || data.suggestions || [];
    suggestions.forEach(item => {
        const li = document.createElement('li');
        li.textContent = item;
        li.className = 'mb-2';
        suggestionsList.appendChild(li);
    });
    

    document.getElementById('resultSection').classList.add('show');
    

    document.getElementById('resultSection').scrollIntoView({ 
        behavior: 'smooth', 
        block: 'nearest' 
    });
}


function copyResults() {
    const title = document.getElementById('resultTitle').textContent;
    const description = document.getElementById('resultDescription').textContent;
    
    const highlights = Array.from(document.getElementById('resultHighlights').children)
        .map((li, index) => `${index + 1}. ${li.textContent}`)
        .join('\n');
    
    const suggestions = Array.from(document.getElementById('resultSuggestions').children)
        .map((li, index) => `${index + 1}. ${li.textContent}`)
        .join('\n');
    
    const fullText = `
TIÊU ĐỀ:
${title}

MÔ TẢ:
${description}

ĐIỂM NỔI BẬT:
${highlights}

GỢI Ý SỐ HÓA 3D:
${suggestions}
    `.trim();
    
    navigator.clipboard.writeText(fullText).then(() => {
        const btn = event.target;
        const originalText = btn.innerHTML;
        btn.innerHTML = '<i class="fas fa-check"></i> Đã sao chép!';
        btn.classList.remove('btn-outline-primary');
        btn.classList.add('btn-success');
        
        setTimeout(() => {
            btn.innerHTML = originalText;
            btn.classList.remove('btn-success');
            btn.classList.add('btn-outline-primary');
        }, 2000);
    }).catch(err => {
        alert('Không thể sao chép: ' + err);
    });
}


function resetForm() {
    document.getElementById('projectForm').reset();
    document.getElementById('resultSection').classList.remove('show');
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Demo mode - nếu không có backend, hiển thị dữ liệu mẫu
// Uncomment phần này để test giao diện mà không cần backend
/*
document.getElementById('projectForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    document.getElementById('loadingSpinner').classList.add('show');
    document.getElementById('resultSection').classList.remove('show');
    
    // Giả lập delay của API
    await new Promise(resolve => setTimeout(resolve, 2000));
    
    // Dữ liệu mẫu
    const demoData = {
        tieu_de: "Căn hộ cao cấp Vinhomes - Không gian sống hiện đại cho gia đình trẻ",
        mo_ta_ngan: "Trải nghiệm không gian sống đẳng cấp với thiết kế hiện đại, tối ưu công năng và ánh sáng tự nhiên. Căn hộ được thiết kế tinh tế, phù hợp hoàn hảo cho gia đình trẻ năng động.",
        diem_noi_bat: [
            "Thiết kế mở tối ưu hóa không gian và ánh sáng tự nhiên",
            "Nội thất cao cấp với phong cách hiện đại, tối giản",
            "View toàn cảnh thành phố từ phòng khách và phòng ngủ chính",
            "Hệ thống smarthome tích hợp đầy đủ",
            "Khu vực vui chơi an toàn cho trẻ em"
        ],
        goi_y_so_hoa: [
            "Chụp toàn cảnh phòng khách với góc rộng để thể hiện không gian mở",
            "Tập trung vào các chi tiết nội thất cao cấp và hệ thống ánh sáng",
            "Chụp view từ cửa sổ và ban công vào golden hour",
            "Thể hiện rõ layout tổng thể của căn hộ qua floor plan 3D",
            "Tạo virtual tour để khách hàng có thể tự khám phá không gian"
        ]
    };
    
    document.getElementById('loadingSpinner').classList.remove('show');
    displayResults(demoData);
});
*/
