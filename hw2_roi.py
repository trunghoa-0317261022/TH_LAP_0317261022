# Nhập vốn ban đầu

initial = float(input("vốn ban đầu: "))

final = float(input("tiền sau khi bán ra: "))

# Lãi nhuận ròng

profit = final - initial

# Roi

roi = (profit / initial) * 100

print("--- Kết quả dự phóng ---")

print(f"Lãi nhuận ròng: {profit:.2f} VNĐ")

print(f"ROI: {roi:.2f}%")