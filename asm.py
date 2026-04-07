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

mean_val = df['Diem_TB'].mean()
df['Diem_TB'] = df['Diem_TB'].fillna(mean_val)

median_val = df['Thu_nhap_thang'].median()
df['Thu_nhap_thang'] = df['Thu_nhap_thang'].fillna(median_val)

if 'Loai_nha' in df.columns:
    mode_val = df['Loai_nha'].mode()[0]
    df['Loai_nha'] = df['Loai_nha'].fillna(mode_val)

df['Ho_Ten'] = df['Ho_Ten'].ffill()

# 5. Kiểm tra lại xem còn ô trống nào không
print("Kết quả sau khi điền Missing Values")
print(df.isnull().sum())
print("5 dòng dữ liệu đầu tiên")
print(df.head())






if 'Gia_nha' in df.columns:
    df = df[df['Gia_nha'] > 0]
    
if 'So_phong' in df.columns:
    df = df[df['So_phong'] > 0]

if 'Loai_nha' in df.columns:
    df['Loai_nha'] = df['Loai_nha'].replace({
        'Chung cu': 'Chung cư',
        'Nha pho': 'Nhà phố',
        'nha pho': 'Nhà phố'
    })

df = df[df['Tuoi'] < 60] # Chỉ lấy người dưới 60 tuổi
df = df[df['Thu_nhap_thang'] < 100] # Chỉ lấy thu nhập dưới 100 triệu

print("--- Dữ liệu sau khi xử lí không hợp lệ")
print(df.head())







so_luong_trung = df.duplicated().sum()
print(f"Số lượng dòng bị trùng lặp ban đầu: {so_luong_trung}")

df.drop_duplicates(keep='first', inplace=True)

print(f"Số lượng dòng sau khi xử lý trùng lặp: {len(df)}")
print("--- 5 dòng dữ liệu sau khi làm sạch trùng lặp")
print(df.head())

