#lab6
#1
n=int(input("nhap so phan tu trong mang"))
bang=[]
for i in range(n):
    a=int(input("nhap so nguyen duong"))
    bang.append(a)
tong_chan=0
tong_le=0
for a in bang:
    if a%2==0:
        tong_chan+=a
    else:
        tong_le+=a
print("tong cac so chan", tong_chan)
print("tong cac so le", tong_le)
#2
n=int(input("nhap so phan tu trong mang"))
bang=[]
for i in range(n):
    a=int(input("nhap so nguyen duong"))
    bang.append(a)
def so_nguyen_to(a):
    flag=True
    if a<2:
        flag=False
    else:
        for i in range(2,a):
            if a%i==0:
                flag=False
                break
    return flag
def so_hoan_hao(a):
    flag=False
    if a<=0:
        return Flag
    else:
        tong=0
        for i in (1,n):
            if n%i==0:
                tong+=1
            if tong==n:
                flag=True
            return flag
nguyen_to=[]
hoan_hao=[]
for a in bang:
    if so_nguyen_to(a):
        nguyen_to.append(a)
    if so_hoan_hao(a):
        hoan_hao.append(a)
print("cac so nguyen to", nguyen_to)
print("cac so hoan hao", hoan_hao)
#3
n=input("nhap day so cach nhau bang khaong trang:").split()
n=[float(a) for a in n ]
max_number=max(n)
min_number=min(n)
print("so lon nhat la:", max_number)
print("so nho nhat la:", min_number)
#4
#a
n=int(input("nhap so luong so Fibonancci muon tao:"))
fib_list=[0,1]
[fib_list.append(fib_list[-2]+fib_list[-1]) for _ in range(n-2)]
print(" day fibnancci dau tien co", n, "so la:", fib_list[:n])
#b
so_nguyen_to=[a for a in range(2,100) if all(a%i !=0 for i in range(2,a))]
print("danh sach cac so nguyen to nho hon 100 la:", so_nguyen_to)
#5
n=input("nhap day so cach nhau bang khoang trang:").split()
n=[int(num) for num in n]
if len(n)<2:
    print("nhap lai")
else:
    sai_so=n[1]- n[0]
    flag=True
    for i in range(1, len(n)-1):
        if n[i +1] -n[i]!= sai_so:
            flag=False
            break       
if flag:
    print("day so", n, "tao thanh cap so cong")
else:
    print("day so", n, "khong tao thanh cap so cong")
#6
#6.1
m1 = int(input("Nhập số hàng của ma trận: "))
n1 = int(input("Nhập số cột của ma trận: "))
matran1 = []
print("Nhập các phần tử của ma trận:")
for i in range(m1):
    row = []
    for j in range(n1):
        row.append(float(input("Nhập phần tử ở hàng {} cột {}: ".format(i + 1, j + 1))))
    matran1.append(row)

tong = 0
for row in matran1:
    tong += sum(row)
print("\nTổng của ma trận:", tong)

m2 = int(input("\nNhập số hàng của ma trận thứ hai: "))
n2 = int(input("Nhập số cột của ma trận thứ hai: "))
matran2 = []
print("\nNhập các phần tử của ma trận thứ hai:")
for i in range(m2):
    row = []
    for j in range(n2):
        row.append(float(input("Nhập phần tử ở hàng {} cột {}: ".format(i + 1, j + 1))))
    matran2.append(row)

if n1 != m2:
    print("\nKhông thể tính tích của hai ma trận với kích thước không phù hợp.")
else:
    tich = []
    for i in range(m1):
        row = []
        for j in range(n2):
            total = 0
            for k in range(n1):
                total += matran1[i][k] * matran2[k][j]
            row.append(total)
        tich.append(row)
    print("\nTích của hai ma trận:")
    for row in tich:
        print(row)

chuyen_vi = [[matran1[j][i] for j in range(len(matran1))] for i in range(len(matran1[0]))]
print("\nMa trận chuyển vị của ma trận ban đầu:")
for row in chuyen_vi:
    print(row)


          
