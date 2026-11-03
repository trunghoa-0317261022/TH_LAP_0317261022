# nhap lieu

no_cong = 1000000000
t = 12
lai = 0.12

print("=" * 50)
print("=== Tinh lai suat ngan hang ===")
print("=" * 50)

def tinh_lai_suat(no_cong, t, lai): #khai bao ham tinh lai suat ngan hang
    """
    Tinh lai suat ngan hang
    no_cong: so tien vay
     t: so thang vay
    lai: lai suat hang thang
     """
    lai_thang = lai / 12.   #chia lai nam ve lai thang
    emi = no_cong * (lai_thang * (1 + lai_thang) ** t) / ((1 + lai_thang) ** t - 1) # cong thuc emi
    tong_lai = emi * t - no_cong # tinh lai chu ki
    return emi, tong_lai

emi, tong_lai = tinh_lai_suat(no_cong, t, lai)
       
print(f"So lai hang thang la: {emi:,.0f} VND " "|" f" Tong lai phai tra la: {tong_lai:,.0f} VND")
print("=" * 50)
