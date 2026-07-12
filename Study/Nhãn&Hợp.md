# NHÃN & HỘP — Bộ Máy Tư Duy Để Đọc Mọi Đoạn Code Python

> Tài liệu này hoàn thiện và mở rộng 2 file gốc: `A=B & A.B` và `Parameters&Arguments`.
> Mục tiêu duy nhất: cho bạn **một bộ luật cố định, cực ít, lặp đi lặp lại** — để dù trí nhớ không tốt, bạn vẫn có thể tự bóc tách logic của bất kỳ đoạn code Python nào, kể cả code bạn chưa từng thấy, mà không cần tra docs.
> Vì bạn giỏi toán, tài liệu này sẽ nói thẳng: một biến Python không phải là một "hộp chứa giá trị". Nó là một **ánh xạ (mapping)** — một cái tên trỏ tới một đối tượng. Toàn bộ Python chỉ là trò chơi của ánh xạ này lặp lại ở nhiều tầng khác nhau.

---

## PHẦN 0 — LUẬT TỐI THƯỢNG (đọc trước khi đọc bất cứ thứ gì khác)

Nếu bạn quên hết tài liệu này, chỉ cần nhớ đúng một câu:

> **Nhãn không chứa gì cả. Nhãn chỉ trỏ tới. Hộp không chứa vật thể, hộp chứa các Nhãn.**

Trong C, Java, hay cách người ta hay dạy nhập môn: biến giống một cái hộp, gán giá trị là "bỏ đồ vào hộp". Python **không** hoạt động như vậy.

Cách Python thực sự hoạt động:

1. Một **Vật thể** (Object) — số `5`, chuỗi `"An"`, một `list`, một hàm, một class, một instance — được tạo ra và sống độc lập trong bộ nhớ, không thuộc về ai cả.
2. Một **Nhãn** (Name / biến) chỉ là một cái tên. Bản thân nó rỗng. Việc duy nhất nó làm là **trỏ tới** một Vật thể.
3. Viết `x = 5` **không có nghĩa là** "đặt số 5 vào trong hộp x". Nó có nghĩa là: *"tạo ra vật thể 5, rồi lấy nhãn x buộc dây vào nó."*

```
Nhãn "x"  ────────▶  [ Vật thể: 5 ]
```

Hệ quả cực kỳ quan trọng: **nhiều nhãn có thể cùng trỏ vào một vật thể**, và **một nhãn có thể đổi hướng trỏ sang vật thể khác bất cứ lúc nào**, mà vật thể cũ không hề bị ảnh hưởng. Toàn bộ Phần III phía dưới xoay quanh hệ quả này.

---

## PHẦN I — GIẢI PHẪU MỘT VẬT THỂ (OBJECT)

Mọi thứ trong Python — không ngoại lệ — là một Vật thể. Số, chuỗi, list, hàm, class, module... tất cả đều là Vật thể. Mỗi Vật thể luôn có đúng 3 thuộc tính cố định:

| Thuộc tính | Ý nghĩa | Cách xem |
|---|---|---|
| **Định danh (identity)** | "Địa chỉ nhà" duy nhất, không đổi trong suốt vòng đời vật thể | `id(obj)` |
| **Kiểu (type)** | Vật thể này thuộc loại gì | `type(obj)` |
| **Giá trị (value)** | Nội dung bên trong nó là gì | `print(obj)` |

```python
x = [1, 2, 3]
print(id(x))     # một con số — "địa chỉ nhà" của vật thể list này
print(type(x))   # <class 'list'>
```

Ghi nhớ `id()` — bạn sẽ dùng nó liên tục để kiểm chứng "hai nhãn này có đang trỏ vào CÙNG một vật thể không".

---

## PHẦN II — BA PHÉP TOÁN GỐC

Đây là 3 quy tắc từ file gốc của bạn, giữ nguyên tinh thần, bổ sung ví dụ code thật để bạn thấy nó vận hành thế nào trên thực tế.

---

### II.1 — `A = B`

**Cú pháp :** `A = B`

**Hành động cốt lõi :** Dán nhãn (Binding)

**Ý nghĩa trong ngôn ngữ tự nhiên :** Lấy nhãn A dán vào vật thể B.

**Ví dụ :**
```python
ten = "An"
```
```
Nhãn "ten"  ────────▶  [ Vật thể: "An" ]
```

---

### II.2 — `A . B`

**Cú pháp :** `A . B`

**Hành động cốt lõi :** Mở hộp (Access)

**Ý nghĩa trong ngôn ngữ tự nhiên :** Mở hộp A ra, tìm và lấy cái đồ vật tên B ở bên trong.

**Ví dụ :**
```python
class Xe:
    banh_xe = 4

xe1 = Xe()
print(xe1.banh_xe)   # Mở hộp xe1, tìm nhãn "banh_xe" bên trong, lấy vật thể 4 ra
```

Ghi chú quan trọng: "Hộp A" ở đây không nhất thiết là một biến bạn tự đặt — nó có thể là một instance, một class, một module, hay bất kỳ vật thể nào **có khả năng chứa nhãn bên trong nó** (Python gọi khả năng này là *namespace*).

---

### II.3 — `A.B = C`

**Cú pháp :** `A.B = C`

**Hành động cốt lõi :** Mở hộp + Dán nhãn

**Ý nghĩa trong ngôn ngữ tự nhiên :** Mở hộp A ra, lấy nhãn B (tạo mới nếu chưa có, hoặc tháo ra nếu đã có) đem đi dán vào vật thể C.

**Ví dụ :**
```python
xe1.mau_son = "Đỏ"   # Mở hộp xe1, dán nhãn "mau_son" vào vật thể "Đỏ"
```

Ba quy tắc trên là **toàn bộ ngữ pháp gốc** của Python. Mọi thứ phía dưới — hàm, class, module, import — chỉ là ba quy tắc này được lặp lại ở quy mô lớn hơn.

---

## PHẦN III — VẬT THỂ "CỨNG ĐẦU" VÀ VẬT THỂ "MỀM DẺO"

### III.1 — Immutable vs Mutable

Một số vật thể, **sau khi tạo ra thì không thể bị chỉnh sửa nội dung bên trong** — muốn "thay đổi" thì bắt buộc phải tạo vật thể mới toanh rồi dán lại nhãn. Gọi là **Cứng đầu (Immutable)**.

Một số vật thể khác **có thể bị chỉnh sửa nội dung ngay tại chỗ**, giữ nguyên định danh (`id()` không đổi). Gọi là **Mềm dẻo (Mutable)**.

| Cứng đầu (Immutable) | Mềm dẻo (Mutable) |
|---|---|
| `int`, `float`, `bool` | `list` |
| `str` | `dict` |
| `tuple` | `set` |
| `frozenset` | hầu hết instance của class bạn tự viết |

```python
x = 5
x = x + 1
# KHÔNG phải x bị đổi thành 6.
# Python tạo vật thể MỚI là 6, rồi tháo nhãn x khỏi 5, dán sang 6.
```
```python
lst = [1, 2, 3]
lst.append(4)
# lst vẫn là CÙNG một vật thể (id không đổi), chỉ nội dung bên trong nó bị sửa.
```

### III.2 — Hệ quả: Aliasing (2 nhãn, 1 vật thể)

Đây là nguồn gốc của phần lớn "bug ma quái" mà người mới học Python gặp phải. Vì `=` chỉ là dán nhãn — **không hề sao chép vật thể** — nên hai nhãn hoàn toàn có thể cùng trỏ vào một vật thể mềm dẻo:

```python
a = [1, 2, 3]
b = a            # b KHÔNG được tặng một list mới. b chỉ là nhãn thứ 2, dán vào CÙNG vật thể mà a đang trỏ tới!
b.append(4)
print(a)         # [1, 2, 3, 4]  <-- a cũng bị ảnh hưởng, dù ta chưa từng đụng vào "a"
```
```
Nhãn "a"  ────┐
              ├────▶  [ Vật thể: list [1, 2, 3, 4] ]
Nhãn "b"  ────┘
```

Nếu `a` là kiểu cứng đầu (vd. `int`), chuyện này không xảy ra — vì bất kỳ thao tác "thay đổi" nào cũng buộc phải tạo vật thể mới, không đụng gì tới nhãn còn lại.

### III.3 — `is` vs `==`

| Toán tử | So sánh cái gì | Câu hỏi tương đương |
|---|---|---|
| `is` | Định danh | "Đây có phải CÙNG MỘT vật thể (cùng `id()`) không?" |
| `==` | Giá trị | "Nội dung bên trong có giống nhau không, dù có thể là 2 vật thể khác nhau?" |

```python
a = [1, 2, 3]
b = [1, 2, 3]     # b là một vật thể list HOÀN TOÀN MỚI, tình cờ có nội dung giống a
print(a == b)     # True  — nội dung giống nhau
print(a is b)     # False — nhưng là 2 vật thể khác nhau, 2 địa chỉ khác nhau
```

---

## PHẦN IV — HÀM = HỘP TẠM THỜI

*(Mở rộng trực tiếp từ file `Parameters&Arguments.md` của bạn)*

**Tham số (Parameter):** những khung kẹp nhãn trống, được chuẩn bị sẵn bên trong một Hộp Tạm Thời (hàm) khi ta định nghĩa nó (`def`).

**Đối số (Argument):** vật thể thật (hoặc nhãn của vật thể thật) mà ta, từ bên ngoài, ném vào các khung kẹp trống đó khi gọi hàm.

### IV.1 — Đường đi dữ liệu (nhắc lại, có sơ đồ)

```python
x = 5

def cal(x_local):
    y_local = x_local * 67
    return y_local

y = cal(x)
```

```
Bên ngoài:  Nhãn "x" ────▶ [5]

Gọi cal(x):
   → Python mở ra 1 Hộp Tạm Thời mới cho lần gọi này
   → Ném nhãn x (đang trỏ vào [5]) vào khung "x_local"
   → Bên trong hộp: Nhãn "x_local" ────▶ [5]  (CÙNG vật thể 5, không sao chép!)
   → Chạy: y_local = x_local * 67  → tạo vật thể mới [335], dán nhãn "y_local" vào nó
   → return y_local → đưa nhãn y_local ra ngoài, Hộp Tạm Thời bị HỦY (x_local, y_local biến mất)

Bên ngoài:  Nhãn "y" ────▶ [335]   (nhận lại vật thể được return)
```

Lưu ý: `x_local` không phải là bản sao của `x`. Nó là một **nhãn khác, trong một hộp khác, cùng trỏ vào một vật thể**. Đây chính là quy tắc II.1, chỉ đơn giản là xảy ra ở "bên trong" một hộp mới.

### IV.2 — Đối số theo vị trí vs theo tên

```python
def gioi_thieu(ten, tuoi):
    print(f"{ten} - {tuoi} tuổi")

gioi_thieu("An", 20)            # Theo vị trí: khung 1 nhận "An", khung 2 nhận 20
gioi_thieu(tuoi=20, ten="An")   # Theo tên: chỉ đích danh khung nào nhận nhãn nào — thứ tự không còn quan trọng
```

### IV.3 — Giá trị mặc định & Cái Bẫy Kinh Điển

Giá trị mặc định của một tham số **chỉ được tạo ra đúng MỘT LẦN**, ngay tại thời điểm `def` chạy — không phải mỗi lần gọi hàm. Nếu giá trị mặc định đó là một vật thể mềm dẻo (vd. `list`), mọi lần gọi hàm mà không truyền đối số sẽ **dùng chung một vật thể duy nhất**:

```python
def them_vao(item, danh_sach=[]):   # [] này CHỈ được tạo 1 lần, lúc def chạy
    danh_sach.append(item)
    return danh_sach

print(them_vao(1))   # [1]
print(them_vao(2))   # [1, 2]   <-- Không phải [2]! Đây KHÔNG phải bug ngẫu nhiên.
```

Vì sao? Khung `danh_sach` khi không được ai ném đối số vào, mặc định trỏ vào **cùng một vật thể list** được tạo lúc `def`. Vật thể đó mềm dẻo — bị `.append()` sửa đổi tại chỗ qua từng lần gọi, và không ai tạo lại nó.

**Cách sửa chuẩn:**
```python
def them_vao(item, danh_sach=None):
    if danh_sach is None:
        danh_sach = []      # mỗi lần gọi mà không có đối số → tạo vật thể MỚI
    danh_sach.append(item)
    return danh_sach
```

### IV.4 — `*args` và `**kwargs` — "Cái Bao Tải"

**Cú pháp :** `def f(*args): ...`

**Hành động cốt lõi :** Bao tải theo vị trí

**Ý nghĩa trong ngôn ngữ tự nhiên :** Mọi đối số dư ra (không có tên) bị ném vào cùng một cái bao tải, gộp lại thành một `tuple`, rồi dán nhãn `args` vào bao tải đó.

**Cú pháp :** `def f(**kwargs): ...`

**Hành động cốt lõi :** Bao tải theo tên

**Ý nghĩa trong ngôn ngữ tự nhiên :** Mọi đối số dư ra có tên bị gom vào một `dict` (tên → giá trị), rồi dán nhãn `kwargs` vào cái dict đó.

```python
def tong(*so):
    print(so)          # (1, 2, 3) — một tuple
    return sum(so)

tong(1, 2, 3)

def in_thong_tin(**thong_tin):
    print(thong_tin)   # {'ten': 'An', 'tuoi': 20} — một dict

in_thong_tin(ten="An", tuoi=20)
```

### IV.5 — `return` — Hộp Tạm Thời Tự Hủy

Khi hàm chạy tới `return`, chuyện xảy ra theo đúng thứ tự:

1. Xác định vật thể mà nhãn phía sau `return` đang trỏ tới.
2. Đưa **một nhãn duy nhất** trỏ tới vật thể đó ra ngoài (nếu bạn viết `return a, b`, thực chất Python đang gói `a, b` thành một vật thể `tuple` duy nhất rồi trả nhãn đó ra).
3. Hộp Tạm Thời (toàn bộ nhãn cục bộ bên trong hàm) bị hủy hoàn toàn.

Vật thể nào **sống sót** sau khi hộp bị hủy? Chỉ những vật thể mà **còn ít nhất một nhãn khác, từ bên ngoài hộp, đang trỏ vào** — ví dụ vật thể vừa được `return`, hoặc vật thể mềm dẻo bị mutate mà có nhãn ngoài cũng đang trỏ vào nó (như trường hợp bẫy `danh_sach=[]` ở trên).

### IV.6 — Phạm vi (Scope) — Các Tầng Hộp Lồng Nhau (LEGB)

Khi Python gặp một nhãn và cần tìm xem nó trỏ vào vật thể nào, nó tìm theo thứ tự từ hộp nhỏ nhất/gần nhất, mở rộng dần ra ngoài:

```
┌─ Built-in  (hộp lớn nhất — print, len, str, ... có sẵn của Python) ──┐
│  ┌─ Global (hộp của cả file/module đang chạy) ───────────────────┐  │
│  │  ┌─ Enclosing (hộp của hàm cha, nếu có hàm lồng hàm) ───────┐ │  │
│  │  │  ┌─ Local (hộp của hàm hiện đang chạy) ────────────────┐│ │  │
│  │  │  │        tìm nhãn Ở ĐÂY trước tiên                    ││ │  │
│  │  │  └───────────────────────────────────────────────────┘│ │  │
│  │  └─────────────────────────────────────────────────────────┘ │  │
│  └───────────────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────────────┘
```

Tên gọi tắt: **L**ocal → **E**nclosing → **G**lobal → **B**uilt-in. Python luôn tìm từ trong ra ngoài, dừng lại ngay khi tìm thấy nhãn đầu tiên khớp tên.

```python
x = "toàn cục"

def ngoai():
    x = "hàm ngoài"
    def trong():
        print(x)   # không có "x" trong hộp Local (trong) → leo lên hộp Enclosing (ngoai) → thấy "hàm ngoài"
    trong()

ngoai()   # in ra: hàm ngoài
```

---

## PHẦN V — CLASS & OBJECT = KHUÔN ĐÚC & HỘP RIÊNG

### V.1 — `class` tạo ra một Hộp Lớn dùng chung

```python
class Xe:
    banh_xe = 4          # nhãn "banh_xe" nằm trong hộp lớn của class Xe

    def __init__(self, mau):
        self.mau = mau    # xem V.2
```

Câu lệnh `class Xe: ...` tạo ra **một vật thể** (bản thân class cũng là một Vật thể!) — một Hộp Lớn chứa các nhãn dùng chung: method (`__init__`), thuộc tính chung (`banh_xe`).

### V.2 — Khởi tạo instance = Mở một Hộp Riêng Mới

```python
xe1 = Xe("Đỏ")
```

Khi bạn gọi `Xe("Đỏ")`, Python:
1. Tạo một **Hộp Riêng hoàn toàn mới, trống rỗng** dành riêng cho `xe1`.
2. Tự động chạy `__init__` như một lời gọi hàm bình thường (giống Phần IV), với một tham số đặc biệt là `self` — **`self` là nhãn được Python tự động buộc vào chính cái Hộp Riêng vừa tạo**.
3. Dòng `self.mau = mau` bên trong `__init__` **chính là quy tắc II.3**: *"Mở hộp self ra, dán nhãn mau vào vật thể mà tham số mau đang trỏ tới."* → Nhãn `mau` giờ nằm trong Hộp Riêng của `xe1`.

```
Hộp Riêng của xe1:
   "mau"  ────▶  [ Vật thể: "Đỏ" ]
```

### V.3 — Thứ tự tìm nhãn khi viết `xe1.banh_xe`

Khi bạn viết `xe1.banh_xe`, Python áp dụng quy tắc II.2 ("Mở hộp"), nhưng nếu Hộp Riêng của `xe1` không có nhãn đó, nó **tự động leo lên Hộp Lớn của class** để tìm tiếp:

1. Mở Hộp Riêng của `xe1` → có nhãn `banh_xe` không? → Không có (chỉ có `mau`).
2. Leo lên Hộp Lớn của class `Xe` → có nhãn `banh_xe` không? → Có, trỏ vào `4`.
3. Trả về `4`.

**Đây chính là bản chất của Kế Thừa (Inheritance):** một class con chỉ là một Hộp Lớn khác, được Python tự động "leo tiếp" lên tìm nếu class hiện tại không có nhãn cần tìm. Không có gì huyền bí hơn thế.

```python
class PhuongTien:
    def di_chuyen(self):
        print("Đang di chuyển")

class Xe(PhuongTien):    # Xe kế thừa PhuongTien
    pass

xe1 = Xe()
xe1.di_chuyen()
# Hộp riêng xe1: không có "di_chuyen"
# → leo lên hộp Xe: không có
# → leo lên hộp PhuongTien: CÓ! → chạy nó
```

---

## PHẦN VI — MODULE & IMPORT = HỘP KHỔNG LỒ NHẤT

Mỗi file `.py` chính là **một Hộp khổng lồ**, chứa mọi nhãn (biến, hàm, class) được định nghĩa trong file đó.

**Cú pháp :** `import ten_module`

**Ý nghĩa :** Tạo một nhãn `ten_module`, dán vào **CẢ cái Hộp khổng lồ** của file đó. Muốn lấy thứ gì bên trong, bắt buộc phải dùng quy tắc II.2: `ten_module.thu_gi`.

**Cú pháp :** `from ten_module import thu_gi`

**Ý nghĩa :** Mở hộp `ten_module` ra NGAY LẬP TỨC, lấy riêng nhãn `thu_gi` ra, và dán trực tiếp nhãn đó vào hộp nơi bạn đang đứng — không cần tiền tố `ten_module.` nữa.

**Cú pháp :** `import ten_module as m`

**Ý nghĩa :** Giống hệt việc đổi tên nhãn ngay lúc dán: nhãn được đặt tên là `m` thay vì `ten_module`, nhưng vẫn trỏ vào cùng một Hộp khổng lồ đó.

---

## PHẦN VII — THUẬT TOÁN ĐỌC CODE (Sổ Tay Nhãn)

Đây là quy trình thao tác tay, áp dụng được cho **bất kỳ** đoạn code Python nào, dù phức tạp tới đâu:

1. Vẽ một bảng 2 cột: **Nhãn** | **Đang trỏ tới vật thể nào**.
2. Đọc code từ trên xuống dưới, từng dòng.
3. Gặp `=` đơn thuần → **Dán Nhãn** (II.1): thêm/cập nhật một dòng trong bảng.
4. Gặp dấu `.` → **Mở Hộp** (II.2): xác định vật thể đứng trước dấu chấm, tìm nhãn cần lấy bên trong hộp riêng của nó, rồi hộp lớn (class), lặp lại nếu cần (V.3).
5. Gặp lời gọi hàm `f(...)` → **Mở một Hộp Tạm Thời mới**:
   - Vẽ một bảng phụ riêng cho lần gọi này.
   - Ném các đối số vào đúng khung tham số (IV.1, IV.2).
   - Chạy từng dòng bên trong hàm bằng **chính quy trình này** (đệ quy!), nhưng tra bảng phụ (Local) trước, mới leo ra bảng ngoài (Enclosing → Global → Built-in) nếu không tìm thấy (IV.6).
   - Gặp `return` → lấy vật thể đó trả ra ngoài, xóa bảng phụ (IV.5).
6. Gặp `class TenClass: ...` → ghi nhận đây là một Khuôn Đúc (Hộp Lớn), **chưa tạo vật thể nào** cho tới khi có dòng gọi `TenClass(...)`.
7. Gặp `TenClass(...)` → tạo một Hộp Riêng mới trống, chạy `__init__` như bước 5, với `self` tự động trỏ vào Hộp Riêng mới đó (V.2).

---

## PHẦN VIII — VÍ DỤ THỰC HÀNH TOÀN TẬP

```python
class GioHang:
    def __init__(self, ten):
        self.ten = ten
        self.mon_hang = []

    def them(self, mon):
        self.mon_hang.append(mon)

def tao_gio_hang_rong(ten):
    return GioHang(ten)

gio_A = tao_gio_hang_rong("An")
gio_A.them("Táo")
gio_A.them("Chuối")

gio_B = gio_A
gio_B.them("Cam")

print(gio_A.mon_hang)
```

Trace tay từng dòng bằng Sổ Tay Nhãn:

| Dòng | Hành động | Bảng nhãn sau dòng đó |
|---|---|---|
| `gio_A = tao_gio_hang_rong("An")` | Gọi hàm → mở Hộp Tạm Thời → bên trong: `GioHang("An")` chạy → tạo Hộp Riêng mới, `self.ten = "An"`, `self.mon_hang = []` → return Hộp Riêng đó | `gio_A` ──▶ [GioHang: ten="An", mon_hang=[]] |
| `gio_A.them("Táo")` | Mở hộp `gio_A`, chạy `them`, `self` = Hộp Riêng của `gio_A`, `.append("Táo")` sửa list tại chỗ | `gio_A` ──▶ [GioHang: mon_hang=["Táo"]] |
| `gio_A.them("Chuối")` | Tương tự | `gio_A` ──▶ [GioHang: mon_hang=["Táo","Chuối"]] |
| `gio_B = gio_A` | **Dán Nhãn** — `gio_B` KHÔNG tạo hộp mới, chỉ là nhãn thứ 2 trỏ vào CÙNG Hộp Riêng mà `gio_A` đang trỏ | `gio_A`, `gio_B` ──▶ CÙNG [GioHang: mon_hang=["Táo","Chuối"]] |
| `gio_B.them("Cam")` | Mở hộp mà `gio_B` trỏ tới (= hộp của `gio_A`!) → sửa list tại chỗ | Cả 2 nhãn cùng thấy `mon_hang=["Táo","Chuối","Cam"]` |
| `print(gio_A.mon_hang)` | Kết quả: `['Táo', 'Chuối', 'Cam']` | — vì `gio_A` và `gio_B` từ đầu đã luôn là **một vật thể duy nhất** (III.2, áp dụng lên cả instance, không chỉ list) |

---

## PHẦN IX — BẢNG TRA CỨU NHANH (Cheat Sheet 1 Trang)

| Cú pháp | Tên hành động | Ý nghĩa bằng lời |
|---|---|---|
| `A = B` | Dán nhãn | Lấy nhãn A, dán vào vật thể B |
| `A . B` | Mở hộp | Mở hộp A, lấy vật/nhãn tên B ra |
| `A.B = C` | Mở hộp + Dán nhãn | Mở hộp A, lấy nhãn B trong đó, đem dán vào vật thể C |
| `def f(p): ...` | Đúc khuôn Hộp Tạm Thời | Chuẩn bị khung kẹp nhãn tên p, chưa có gì trong đó |
| `f(x)` | Gọi hàm | Ném nhãn x vào khung p, chạy code trong hộp, trả về, rồi hộp bị hủy |
| `return X` | Trả nhãn ra ngoài | Đưa vật thể X ra khỏi hộp, trước khi hộp bị hủy |
| `*args` | Bao tải theo vị trí | Gom mọi đối số dư (không tên) thành 1 `tuple` |
| `**kwargs` | Bao tải theo tên | Gom mọi đối số dư (có tên) thành 1 `dict` |
| `class X: ...` | Đúc Hộp Lớn | Tạo 1 hộp lớn chứa nhãn dùng chung (method, thuộc tính chung) |
| `X(...)` | Mở Hộp Riêng mới | Tạo 1 hộp riêng trống, chạy `__init__` với `self` trỏ vào hộp đó |
| `self` | Nhãn tự trỏ | Luôn trỏ vào Hộp Riêng của vật thể đang được thao tác |
| `import m` | Nhãn trỏ cả hộp | Tạo nhãn m, trỏ vào CẢ hộp module |
| `from m import x` | Mở hộp lấy luôn | Mở hộp module m, lấy riêng nhãn x, dán thẳng ra ngoài |
| `is` | So sánh định danh | Có phải CÙNG một vật thể (cùng `id()`) không |
| `==` | So sánh giá trị | Nội dung có giống nhau không (dù có thể khác vật thể) |
| Mutable (`list`, `dict`, `set`, instance) | Vật thể mềm dẻo | Sửa được tại chỗ, `id()` không đổi → coi chừng aliasing |
| Immutable (`int`, `str`, `tuple`,...) | Vật thể cứng đầu | "Sửa" = tạo vật thể mới + dán lại nhãn |

---

## Lời kết

Từ giờ, mỗi khi gặp một đoạn code Python — dù dài, dù lạ, dù chưa từng thấy thư viện đó bao giờ — bạn chỉ cần tự hỏi lặp đi lặp lại đúng 3 câu:

1. *Đây có phải đang **Dán Nhãn** không?*
2. *Đây có phải đang **Mở Hộp** không?*
3. *Đây có phải đang **mở một Hộp Tạm Thời** (gọi hàm/tạo instance) không?*

Ba câu hỏi đó, lặp lại đủ số lần, bóc tách được logic của bất kỳ đoạn code Python nào — vì bản thân Python, ở tầng sâu nhất, chỉ được xây từ ba thao tác đó mà thôi.
