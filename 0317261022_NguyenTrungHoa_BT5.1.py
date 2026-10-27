# nhap lieu

tuoi = 25
so_du = 0
tien_gui = 60000000
lai = 0.1
tien_gui_tang = 0.08 
muc_tieu = 10000000000
nam = 1
""""""
print("=== BÁO CÁO MÔ PHỎNG KẾ HOẠCH HƯU TRÍ TỰ ĐỘNG ===")

print("Muc Tieu: 10ty VND")

print(f"{'Năm':<6} | {'Tuổi':<6} | {'Tiền gửi năm nay (VND)':>25} | {'Tiền lãi năm nay (VND)':>25} | {'Số dư cuối năm (VND)':>25}")

print("-" * 100)

""""""
while so_du < muc_tieu:
    # tinh tien lai va so du
    tien_lai = so_du * lai
    # cap nhat so du
    so_du += tien_lai + tien_gui 
    
    
    print(f"{nam:<6} | {tuoi:<6} | {tien_gui:>25,.0f} | {tien_lai:>25,.0f} | {so_du:>25,.0f}") 

    tuoi += 1
    nam += 1 
    # tien gui nam sau tang 8%
    tien_gui = tien_gui * (1 +tien_gui_tang)
print("-" * 100)
print(f"Kết luận khách hàng sẽ đạt được mục tiêu 10 tỷ VND sau {nam-1} năm, khi tuổi {tuoi-1}.")
print("=== Lịch sử tăng trưởng tài khoản ===")

