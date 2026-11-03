# nhap lieu

income = int(input("Nhap thu nhap hang thang: "))
credit_history_years = int(input("Nhap so nam lich su tin dung: "))
has_bad_debt = int(input("Co no xau khong? (nhap 1 neu co, 0 neu khong): "))

if has_bad_debt == 1:
    has_bad_debt = True
else:
    has_bad_debt = False

def credit_score(income, credit_history_years, has_bad_debt = False):
    if has_bad_debt == True: # neu has = true thì tra ve Reject
        return "Reject"

    elif income < 10000000 or credit_history_years < 1:  
        return "High Risk"

    elif income >= 20000000 and credit_history_years >= 3:
        return "VIP"

    else:
        return "Standard"

print("=" * 50)
print("=== Kiem tra diem tin dung ===")
print("=" * 50)

result = credit_score(income, credit_history_years, has_bad_debt) # goi ham credit_score de kiem tra diem tin dung
if result == "Reject":
    print("Khong duoc chap nhan vay")
elif result == "High Risk":
    print("Nguy co cao")
elif result == "VIP":
    print("Khach hang VIP, duoc chap nhan vay")
else:
    print("Khach hang binh thuong, duoc chap nhan vay")