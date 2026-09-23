print("---- Công cụ tính lãi suất tiết kiệm ----")

# 1. Nhập liệu và ép kiểu

principal = float(input("Nhập số tiền gốc(VND): "))
rate = float(input("Nhập lãi suất hằng năm(vd: 0.07 cho là 7%): "))
years = int(input("Nhập số năm gửi: "))

# 2. Tính toán
# Lãi đơn: Chỉ tính phần tiền lãi sinh ra

simple_interest = principal * rate * years

# Lãi kép: Tính tổng tiền (Gốc + Lãi) nhập vốn sinh lời

compound_total = principal * (1 + rate) ** years

# Lãi kép ròng = Tổng tiền - Gốc ban đầu

compound_interest = compound_total - principal

# 3. Xuất kết quả 

print("\n--- KẾT QUẢ DỰ PHÓNG ---")
print(f"Tiền lãi nhận được (Lãi đơn): {round(simple_interest):,.0f} VND")
print(f"Tiền lãi nhận được (Lãi kép): {round(compound_interest):,.0f} VND")
print(f"Sự chênh lệch: {round(compound_interest - simple_interest):,.0f} VND")