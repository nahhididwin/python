# Tạo một hàm xử lý lỗi chung để tái sử dụng
def xu_ly_loi_chung(e):
    print(f"[NHẬT KÝ] Phát hiện lỗi hệ thống: {e}")
    # Bạn có thể ghi lỗi vào file, gửi tin nhắn báo động... ở đây

# Mỗi hành động có try-except riêng nhưng dùng chung hàm xử lý
try: # example 1: lỗi chia cho 0
    loi_b1 = 10 / 0
except Exception as e:
    xu_ly_loi_chung(e)

try: # example 2: lỗi kiểu dữ liệu
    loi_b2 = int("không phải số")
except Exception as e:
    xu_ly_loi_chung(e)
# Exception là cho python tự xác định lỗi (automatically);

