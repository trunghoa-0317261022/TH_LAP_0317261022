# nhap lieu
goc = 20.0 
list_ex = [-0.03, 0.0, 0.03]  
list_ir = [-0.02, -0.01, 0.01, 0.02]  

print("=== MA TRẬN PHÂN TÍCH ĐỘ NHẠY GIÁ TRỊ DANH MỤC (TỶ VNĐ) ===")
print(f"Vốn danh mục ban đầu: {goc:.2f} Tỷ VNĐ\n")

print(f"{'Thay đổi Lãi suất (Dòng) \\ Tỷ giá (Cột)':<42} | {'-3.0%':<9} | {'0.0%':<9} | {'+3.0%':<9}")
print("-" * 74)

for delta_ir in list_ir:
    # đổi sang phần trăm, thêm dấu + nếu lớn hơn 0
    if delta_ir > 0:
        ir_str = f"+{delta_ir*100:.1f}%"
    else:
        ir_str = f"{delta_ir*100:.1f}%"
    row_label = f"Lãi suất: {ir_str}"
    
    row_output = f"{row_label:<42} | "

    for delta_ex in list_ex:
        # tinh danh muc moi
        v_moi = goc * (1 + 1.5 * delta_ex - 2.0 * delta_ir)  
        # dinh dang gia 
        row_output += f"{v_moi:>6.2f} Tỷ | "

    print(row_output[:-2])  
print("-" * 74)