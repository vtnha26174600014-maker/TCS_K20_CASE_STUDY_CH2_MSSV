tong_phut = 135
cong_suat_w = 250

tong_gio = tong_phut // 60
phut_con_lai = tong_phut % 60

print("Số giờ:", tong_gio)
print("Số phút còn lại:", phut_con_lai)

su_dung_lau = tong_phut > 60
print("Sử dụng lâu:", su_dung_lau)

du_lieu_hop_le = cong_suat_w > 0 and tong_phut > 0
print("Dữ liệu hợp lệ:", du_lieu_hop_le)

print("100 + 20 * 3 =", 100 + 20 * 3)
print("(100 + 20) * 3 =", (100 + 20) * 3)