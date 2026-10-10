# Bài 3: Trích xuất Dữ liệu Giao dịch Tài chính

ma_giao_dich = "GD001-5000000-VND"

# Tách chuỗi bằng dấu gạch ngang (-) thành một danh sách các phần

# Phần tử thứ 2 (chỉ số là 1) chính là số tiền: "5000000"

so_tien = int(ma_giao_dich.split("-")[1])

if so_tien >= 5000000:

  print("Giao dịch cần xác thực OTP")

else:

  print("Giao dịch thành công")