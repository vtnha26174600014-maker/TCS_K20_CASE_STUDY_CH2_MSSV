cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("Điện năng tiêu thụ:", dien_nang_kwh, "kWh")
print("Chi phí điện:", chi_phi, "VND")

so_phut = 60

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("Sau khi thay thời gian bằng 60 phút:")
print("Điện năng tiêu thụ:", dien_nang_kwh, "kWh")
print("Chi phí điện:", chi_phi, "VND")