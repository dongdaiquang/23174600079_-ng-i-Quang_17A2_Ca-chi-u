#lab 5
#1
n=int(input("nhap so nguyen duong:"))
if n<=0:
    print("hu cau")
else:
    danh_sach=""
    while n>0:
        a=str(n%2)
        danh_sach=a+danh_sach
        n=n//2
    print("so nhi phan tuong ung:", danh_sach)
#2
str1=input("nhap chuoi 1:")
str2=input("nhap chuoi 2:")
m = len(str1)
n = len(str2)
dp = [[0]*(n + 1) for _ in range(m + 1)]
max_length = 0
end_index = 0
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            if dp[i][j] > max_length:
                max_length = dp[i][j]
                end_index = i
        else:
            dp[i][j] = 0
if max_length == 0:
    print("Không có chuỗi con chung.")
else:
    result = str1[end_index - max_length: end_index]
    print("Chuỗi con chung ngắn nhất là:", result)
#3
n=input("nhap chuoi van ban")
m=input("nhap tu can tim kiem")
count_overlap=0
start=0
a=-1
for i in range(len(n)):
    if n[i]==m:
        a=1
        print("vi tri cua ky tu trong chuoi la:",a)
        break
if a==-1:
    print("khong co ky tu trong chuoi")
while True:
    start=n.find(m, start)
    if start==-1:
        break
    count_overlap += 1
    start+=1
if count_overlap==0:
    print("khong lam trong chuoi")
else:
    print("co lam trong chuoi")
    print("so lan xuat hien:", count_overlap)
#4
n=input("nhap chuoi tu ban phim")
n1=n
n2=""
for i in n1:
    if i.isnumeric()== False:
        n1=n1.replace(i,"")
print(n1)
if n1:
    n3=int(n1)
    if n3<2:
        flag=False
    else:
        flag=True
        for i in range(2,n3):
            if n3%i==0:
                flag=True
                break
    if flag:
        print(n3, "la so nguyen to")
    else:
        print(n3, "khong la so nguyen to")
else:
    print("khong co so nao trong ky tu da cho")
#5
str1=input("nhap chuoi 1")
str2=input("nhap chuoi 2")
chuoi_tron=""
min_length=0
if len(str1)>len(str2):
    min_length=len(str2)
else:
    min_length=len(str1)
for i in range(min_length):
    chuoi_tron+= str1[i] +"-"+str2[i]+ "-" 
if len(str1)>len(str2):
    chuoi_tron=chuoi_tron+"-"+str1[min_length:]
else:
    chuoi_tron=chuoi_tron+"-"+str2[min_length:]
chuoi_tron=chuoi_tron[:-2]
print("''", chuoi_tron, "''")
#6
input_string = input("Nhập chuỗi: ")
total_chars = len(input_string)
special_chars_count = 0
print("Các ký tự đặc biệt trong chuỗi và số lần xuất hiện của chúng:")
for char in input_string:
    if not char.isalnum():
        count = input_string.count(char)
        if char not in input_string[:input_string.index(char)]:
            special_chars_count += count
            print(f"'{char}': {count}")
print("/n ty le phan tram cua moi phan tu dac biet")
for char in input_string:
    if not char.isalnum():
        count = input_string.count(char)
        if char not in input_string[:input_string.index(char)]:
            percentage = (count / total_chars) * 100
            print(f"'{char}': {percentage:.2f}%")
#7
n=input("nhap chuoi:")
a=0
b=0
c=0
d=0
for char in n:
    if char.islower():
        a += 1
    elif char.isupper():
        b += 1
    elif char.isdigit():
        c += 1
    else:
        d += 1
print("so luong chu thuong",a)
print("so luong chu hoa",b)
print("so luong chu so",c)
print("so luong ky tu dac biet",d)
#8
n=input("nhap chuoi:")
if len(n)<10:
    print("nhap lai chuoi")
else:
    str1=n[1:8]
    print("a:", str1)
    str2=n[4:9]
    print("b:", str2)
    str3=n[-1:-4:-1]
    print("c:", str3)
    str4=n.lower()
    print("d:", str4)
    str5=n.upper()
    print("e:", str5)
    str6=n[::-1]
    print("f", str6)
#10
m=input("nhap chuoi:")
print("chuoi sau khi bi xoa khoang trang:", m.replace(" ",""))
