# Chia tiền hoá đơn

tongbill = float(input("Nhập tổng tiền hóa đơn: "))

tip      = tongbill * 5 / 100

so_nguoi = int(input("Nhập số người chia: ")) 

tien_moi_nguoi = (tongbill + tip) / so_nguoi

print(f"Mỗi người phải trả: {tien_moi_nguoi:.2f} VNĐ")