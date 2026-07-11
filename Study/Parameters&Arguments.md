Giải thích chi tiết cách mà tham số & đối số hoạt động. Tham số & đối số liên quan đến function và tồn tại trong các class, module, library, def,...v.v ; Và logic, đường đi dữ liệu của nó,..etc;


Tham số (Parameter): Là những "Khung kẹp nhãn trống" được chuẩn bị sẵn bên trong một cái Hộp Tạm Thời (Hàm/Phương thức) khi ta định nghĩa nó (def).

Đối số (Argument): Là Đồ vật thật (hoặc nhãn của đồ vật thật) ta đứng từ bên ngoài ném vào các khung kẹp trống đó khi gọi hàm.


**1. Đường đi dữ liệu trong Hàm (def)**

Hãy nhìn cách dữ liệu di chuyển từ ngoài vào trong một hàm thông thường:

Pseudocode :

x = input()

def cal(x_local):
  y_local = x_local * 67
  return y_local

y = cal(x)


































