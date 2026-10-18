from datetime import datetime

ma_phien = input("Nhập mã phiên: ")
ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhập công suất thiết bị (W): "))
so_phut = int(input("Nhập thời gian sử dụng (phút): "))
don_gia_kwh = float(input("Nhập đơn giá điện (VND/kWh): "))

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
su_dung_lau = so_phut > 60

thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")

print(f"Mã phiên: {ma_phien}")
print(f"Máy: {ma_may}")
print(f"Công suất: {cong_suat_w:.2f} W")
print(f"Thời lượng: {so_phut} phút")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")
print(f"Chi phí: {chi_phi:.2f} VND")
print(f"Trên 60 phút: {su_dung_lau}")
print(f"Ghi nhận lúc: {thoi_diem_text}")