
ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhập công suất W: "))
so_phut = int(input("Nhập số phút: "))

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000

print(f"Mã máy: {ma_may}")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")

# Lỗi thứ nhất: input() trả về chuỗi nên cần dùng float() để chuyển công suất sang số.
# Lỗi thứ hai: phải dùng đúng tên biến dien_nang_kwh trong câu lệnh print().