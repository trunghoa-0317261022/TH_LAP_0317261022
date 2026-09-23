print("--- GIỎ HÀNG CỦA BẠN ---")

# Nhập giá trị của 3 sản phẩm

item1 = float(input("Nhập giá sản phẩm 1: "))
item2 = float(input("Nhập giá sản phẩm 2: "))
item3 = float(input("Nhập giá sản phẩm 2: "))

discount_rate = float(input("Nhập % mã giảm giá (vd: 10 cho 10%): ")) / 100
VAT_RATE = 0.08 # Thuế VAT 8%

# Tính toán các thành phần 

subtotal = item1 + item2 + item3
discount_amount = subtotal * discount_rate
price_after_discount = subtotal - discount_amount
vat_amount = price_after_discount * VAT_RATE
final_total = price_after_discount + vat_amount

# Hiển thị hóa đơn

print("\n--- HÓA ĐƠN ĐIỆN TỬ ---")
print(f"Tạm tính        : {round(subtotal):,.0f} VND")
print(f"Giảm giá        : -{round(discount_amount):,.0f} VND")
print(f"Thuế VAT (8%)   : +{round(vat_amount):,.0f} VND")
print("_" * 25)
print(f"Tổng thanh toán:   {round(final_total):,.0f} VND")