# Thông tin khách hàng

count = "NguyenVanA@gmai.com"

# tách chuỗi split

count2 = count.split("@")

ten = count2[0]

gmail = count2[1]

ten2 = ten[0:3]

gmail2 = gmail[0:1]

# che lại thông tin khách hàng

masker = ten[0:4] + "*" * (len(ten) - 4) + "@" + gmail 

# xuất ra màn hình

print(masker)