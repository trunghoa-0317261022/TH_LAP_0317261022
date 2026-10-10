# Bài 1: Phân loại Hạn mức Rủi ro Tín dụng

diem_credit = 780  # Bạn có thể thay đổi số điểm này để test

if 750 <= diem_credit <= 850:

  print("Rủi ro Thấp - Duyệt tự động")

elif 600 <= diem_credit < 750:

  print("Rủi ro Trung bình - Cần thẩm định")

else:

  print("Rủi ro Cao - Từ chối cấp tín dụng")