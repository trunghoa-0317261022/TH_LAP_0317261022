# nhap lieu

F = 1000000
c = 0.09
N = 10
Y = 0.085

# tinh lai coupon hang nam
C = F * c

print("=" * 65)
print(f"{'BÁO CÁO ĐỊNH GIÁ TRÁI PHIẾU DOANH NGHIỆP':^65}")
print("=" * 65)
print(f"- Mệnh giá trái phiếu (F): {F:,.0f} VNĐ")
print(f"- Lãi suất coupon (c): {c*100}%/năm -> Tiền lãi hàng năm (C): {C:,.0f} VNĐ")
print(f"- Thời hạn trái phiếu (N): {N} năm")
print(f"- Lợi suất kỳ vọng thị trường (Y): {Y*100}%/năm")
print("-" * 65)
print(f"{'Năm (t)':<10} | {'PV Tiền lãi coupon (VNĐ)':<25}")
print("-" * 65)

tong_pv = 0
for t in range(1, N + 1):
    PV_coupon = C / (1 + Y) ** t
    tong_pv += PV_coupon
    print(f"{t:<10} | {PV_coupon:>25,.0f}")
print("-" * 65)

PV_menh_gia = F / (1 + Y) ** N
trai_phieu = tong_pv + PV_menh_gia

if trai_phieu > F:
    trang_thai = "Cao hơn mệnh giá (Premium)"
elif trai_phieu < F:
    trang_thai = "Thấp hơn mệnh giá (Discount)"
else:
    trang_thai = "Bằng mệnh giá (Par)"

print(f"- Giá trị hiện tại của mệnh giá trái phiếu (PV_menh_gia): {PV_menh_gia:,.0f} VNĐ")
print(f"- Giá trị hiện tại của trái phiếu (trai_phieu): {trai_phieu:,.0f} VNĐ")
print(f"- Trạng thái trái phiếu: {trang_thai}")
print("=" * 65) 