# Nhập các chi phí ban đầu

chi_phi_co_dinh = float(input("Nhập tổng chi phí cố định (Tiền thuê, máy móc...): "))
gia_ban = float(input("Nhập giá bán ra 1 sản phẩm: "))
chi_phi_bien_doi = float(input("Nhập chi phí nguyên liệu sản xuất 1 sản phẩm: "))

loi_nhuan_gop = gia_ban - chi_phi_bien_doi

# Lấy nguyên để làm tròn số lượng sản phẩm lên

so_luong_hoa_von = chi_phi_co_dinh // loi_nhuan_gop
print(f"Bạn cần bán tối thiểu {int(so_luong_hoa_von + 1)} sản phẩm để bắt đầu có lãi.")