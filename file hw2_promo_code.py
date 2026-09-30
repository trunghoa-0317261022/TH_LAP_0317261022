# Nhập họ về tên khách hàng

hovaten = "Lê Văn A"

namsinh = 1990

hoten = hovaten.split(" ")

hoten1 = hoten[0] 

hoten2 = hoten[1]

hoten3 = hoten[2]

# sling

ten = hoten3[0:1]

tenlot = hoten2[0:1]

ho = hoten1[0:1]

#xuất ra màn hình

hovaten1 = f"{ho}{tenlot}{ten}".upper()

print(f"Kết quả: {hovaten1}-{namsinh}-VIP ")
