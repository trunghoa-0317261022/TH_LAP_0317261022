#1. Khai báo tỷ giá → Quy ước: Hằng số viết HOA

RATE_USD_VND = 25450.5
RATE_EUR_VND = 27800.0
print("--- HỆ THỐNG KIỀU HỐI FINTECH ---")

# 2. Nhập số lượng ngoại tệ

usd_amount = float(input("Nhập số lượng USD cần đổi: $"))
eur_amount = float(input("Nhập số lượng EUR cần đổi: €"))

# 3. Tính toán

vnd_from_usd = usd_amount * RATE_USD_VND
vnd_from_eur = eur_amount * RATE_EUR_VND
total_vnd = vnd_from_usd + vnd_from_eur

# 4. In biên lai

print("\n--- BIÊN LAI QUY ĐỔI ---")
print(f"Tiền từ USD: {round(vnd_from_usd):,.0f} VND")
print(f"Tiền từ EUR: {round(vnd_from_eur):,.0f} VND")
print("-" * 25)
print(f"TỔNG THỰC NHẬN: {round(total_vnd):,.0f} VND")