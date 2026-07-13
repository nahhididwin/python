
# JIT Compilers

**1. Thư viện Numba (Just-In-Time cho tính toán số học)**

Numba dịch các hàm python sang mã máy trong lần đầu tiên hàm đó được gọi, kiểu vậy.

```python

from numba import njit

@njit(fastmath=True, parallel=True)
def tinh_toan_giga(mang_so):
    # Code tính toán, vòng lặp phức tạp ở đây
    return ket_qua
    
```

Tham số fastmath=True khiến CPU skip một số quy tắc an toàn từ IEEE (hình như là floating point) để nhanh hơn.

parallel=True thì hình như để phân rã vòng lặp ra đa nhân CPU.

Tuy nhiên, chỉ hỗ trợ các kiểu dữ liệu nguyên bản (int, float, array), không hỗ trợ các object tùy biến của Python.

**PyPy (thay thế CPython) :**

Thay vì chạy python script.py; bạn cài PyPy và chạy pypy3 script.py;



# 
