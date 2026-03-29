import pandas as pd
import numpy as np

data = {
    'Ho_Ten': ['An', 'Binh', 'Chi', 'Dung', 'Em', 'Giang', 'Huong', 'Khoa', 'Lan', 'Minh'],
    'Tuoi': [20, 21, 19, 22, 20, 21, 19, 20, 22, 80], 
    'Diem_TB': [7.5, 8.2, 6.5, None, 9.0, 5.5, 8.8, None, 7.2, 10.0],
    'Thu_nhap_thang': [2, 3, 2.5, 4, 3.5, 1, 5, 2.8, 3.2, 500],
    'Khu_vuc' : ['Ha Noi', 'TP HCM', 'Da Nang', 'Ha Noi', 'TP HCM', 'TP HCM', 'Da Nang', 'Ha Noi', 'Ha Noi', 'TP HCM']
}
df = pd.DataFrame(data)


print("Thóng kê mô tả các cột:")
print(df.describe())

print("Kiểm tra dữ liệu thiếu:")
print(df.isnull().sum())

print("Thống kê dữ liệu trùng lặp (Duplicate)")
print(f"Số lượng dòng trùng lặp: {df.duplicated().sum()}")





import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

plt.figure(figsize=(20, 6))

plt.subplot(1, 3, 1)
sns.histplot(df['Thu_nhap_thang'], kde=True, color='skyblue')
plt.title('Biểu đồ Histogram (Phân phối)')
plt.xlabel('Thu nhập')

plt.subplot(1, 3, 2)
sns.boxplot(y=df['Thu_nhap_thang'], color='salmon')
plt.title('Biểu đồ Boxplot (Ngoại lệ)')
plt.ylabel('Thu nhập')

plt.subplot(1, 3, 3)
sns.violinplot(y=df['Thu_nhap_thang'], color='lightgreen')
plt.title('Biểu đồ Violin (Mật độ)')
plt.ylabel('Thu nhập')

plt.tight_layout()
plt.show()







print("Thống kê số lượng thep khu vực")
print(df['Khu_vuc'].value_counts())

plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='Khu_vuc', palette='viridis')
plt.title('Phân phối dữ liệu theo Khu vực (Categorical)')
plt.xlabel('Khu vực')
plt.ylabel('Số lượng')
plt.show()

df['Do_dai_Ten'] = df['Ho_Ten'].apply(len)
print("Thống kê độ dài tên")
print(df[['Ho_Ten', 'Do_dai_Ten']].head())






import pandas as pd
import numpy as np

# Giả sử đây là bảng df từ Ý 1 (có cột Diem_TB và Thu_nhap_thang bị thiếu)
# Mình thực hiện điền thiếu theo đúng các phương pháp đề yêu cầu:

# 1. Điền bằng MEAN (Trung bình): Thường dùng cho dữ liệu số ổn định
# Áp dụng cho cột Diem_TB
mean_val = df['Diem_TB'].mean()
df['Diem_TB'] = df['Diem_TB'].fillna(mean_val)

# 2. Điền bằng MEDIAN (Trung vị): Dùng khi có giá trị ngoại lệ (Outliers)
# Áp dụng cho cột Thu_nhap_thang (vì có ông thu nhập 500 triệu làm sai lệch số trung bình)
median_val = df['Thu_nhap_thang'].median()
df['Thu_nhap_thang'] = df['Thu_nhap_thang'].fillna(median_val)

# 3. Điền bằng MODE (Yếu vị): Dùng cho dữ liệu dạng chữ/phân loại
# Giả sử có cột 'Loai_nha', ta điền giá trị xuất hiện nhiều nhất
if 'Loai_nha' in df.columns:
    mode_val = df['Loai_nha'].mode()[0]
    df['Loai_nha'] = df['Loai_nha'].fillna(mode_val)

# 4. Điền bằng FORWARD FILL (ffill): Lấy giá trị dòng trên điền xuống dòng dưới
# Thường dùng cho dữ liệu có tính thứ tự hoặc thời gian
df['Ho_Ten'] = df['Ho_Ten'].ffill()

# 5. Kiểm tra lại xem còn ô trống nào không
print("Kết quả sau khi điền Missing Values")
print(df.isnull().sum())
print("5 dòng dữ liệu đầu tiên")
print(df.head())







# Giả sử bảng df của bạn có các lỗi sau để thực hành:
# 1. Giá âm (-5 tỷ)
# 2. Số phòng = 0 (Nhà mà không có phòng nào)
# 3. Typo (Viết sai: 'Chung cu' thay vì 'Chung cư')

# --- 2.1 XỬ LÝ GIÁ ÂM VÀ SỐ PHÒNG = 0 ---
# Cách tốt nhất là lọc lấy những dòng có dữ liệu HỢP LỆ (Dương và > 0)
# Giả sử cột là 'Gia_nha' và 'So_phong'
if 'Gia_nha' in df.columns:
    df = df[df['Gia_nha'] > 0]
    
if 'So_phong' in df.columns:
    df = df[df['So_phong'] > 0]

# --- 2.2 XỬ LÝ TYPO TRONG CATEGORICAL ---
# Dùng hàm .replace() để sửa lỗi chính tả hàng loạt
# Ví dụ: sửa 'Chung cu' thành 'Chung cư', 'Nha pho' thành 'Nhà phố'
if 'Loai_nha' in df.columns:
    df['Loai_nha'] = df['Loai_nha'].replace({
        'Chung cu': 'Chung cư',
        'Nha pho': 'Nhà phố',
        'nha pho': 'Nhà phố'
    })

# --- 2.3 XỬ LÝ NGOẠI LỆ (Outliers) CHO TUỔI VÀ THU NHẬP ---
# Như Ý 1 ta thấy có Tuổi = 80 (quá cao cho SV) và Thu nhập = 500 (quá ảo)
# Ta có thể giới hạn lại dữ liệu hợp lệ
df = df[df['Tuoi'] < 60] # Chỉ lấy người dưới 60 tuổi
df = df[df['Thu_nhap_thang'] < 100] # Chỉ lấy thu nhập dưới 100 triệu

print("--- DỮ LIỆU SAU KHI XỬ LÝ KHÔNG HỢP LỆ ---")
print(df.head())







# --- 1. KIỂM TRA DỮ LIỆU TRÙNG LẶP TRƯỚC KHI XỬ LÝ ---
# Lệnh duplicated().sum() cho biết có bao nhiêu dòng bị trùng hoàn toàn
so_luong_trung = df.duplicated().sum()
print(f"Số lượng dòng bị trùng lặp ban đầu: {so_luong_trung}")

# --- 2. LOẠI BỎ CÁC DÒNG TRÙNG LẶP (DROP DUPLICATES) ---
# keep='first': Giữ lại dòng đầu tiên, xóa các dòng trùng phía sau
# inplace=True: Cập nhật trực tiếp vào biến df luôn
df.drop_duplicates(keep='first', inplace=True)

# --- 3. XỬ LÝ TRÙNG LẶP THEO TÊN (NẾU CẦN) ---
# Đôi khi dữ liệu không trùng 100% các cột nhưng trùng cột 'Ho_Ten'
# Ta có thể xóa dựa trên 1 cột cụ thể:
# df.drop_duplicates(subset=['Ho_Ten'], keep='last', inplace=True)

# --- 4. KIỂM TRA LẠI KẾT QUẢ ---
print(f"Số lượng dòng sau khi xử lý trùng lặp: {len(df)}")
print("\n--- 5 DÒNG DỮ LIỆU SAU KHI LÀM SẠCH TRÙNG LẶP ---")
print(df.head())


