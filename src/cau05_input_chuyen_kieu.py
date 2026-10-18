ma_may = input("Nhập mã máy: ")
cong_suat_w = input("Nhập công suất (W): ")
so_phut = input("Nhập số phút sử dụng: ")
don_gia_kwh = input("Nhập đơn giá điện (VND/kWh): ")

print("Kiểu dữ liệu ban đầu:")
print(type(ma_may))
print(type(cong_suat_w))
print(type(so_phut))
print(type(don_gia_kwh))

cong_suat_w = float(cong_suat_w)
so_phut = int(so_phut)
don_gia_kwh = float(don_gia_kwh)

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("Điện năng:", dien_nang_kwh, "kWh")
print("Chi phí:", chi_phi, "VND")