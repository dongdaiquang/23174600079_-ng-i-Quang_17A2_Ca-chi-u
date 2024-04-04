#lab4
#1
bang_so=[]
tong_so_nhap=0
dem=0
while tong_so_nhap<=1000:
    so=int(input("nhap so:"))
    bang_so.append(so)
    tong_so_nhap+=so
    dem+=1
so_le=[so for so in bang_so if so%2!=0]
so_chan=[so for so in bang_so if so%2==0]
print("cac so le la:", so_le)
print("cac so chan la:", so_chan)
print("so nguyen da nhap la", dem)
#2
#a
n=1
while n<100:
    print(n, end=" ")
    n+=1
#b
n=1
while n**n<100:
    print(n**n, end=" ")
    n+=1
#c
#3
n=int(input("nhap so:"))
dem=0
while n>0:
    dem+=1
    n//=10
print("so chu so nguyen la:", dem)
#4
#a
n=int(input("nhap so:"))
if n <= 10:
    print("Vui lòng nhập n lớn hơn 10.")
else:
    a=1
    S1=0
    while True:
        S1+=6**a
        if a>n:
            break
        print("S1", S1)
        a+=1
#b
n=int(input("nhap so:"))
if n<=10:
    print("khong hop le")
else:
    a=1
    S2=0
    while True:
        S2+=1/3**(2*a+1)
        if a>n:
            break
        print("S2", S2)
        a+=1
#c
n=int(input("nhap so:"))
if n<=10:
    print("khong hop le")
else:
    a=1
    S3=0
    while True:
        S3+=((-1)**a)*a**2
        if a>n:
            break
        print("S3", S3)
        a+=1
#d
n=int(input("nhap so:"))
if n<=10:
    print("khong hop le")
else:
    a=1
    S4=0
    while True:
        S4+=a*(a+1)*(a+2)
        if a>n:
            break
        print("S4", S4)
        a+=1
#5
import math
while True:
    n=int(input("nhap so"))
    m=int(input("nhap so"))
    print("cong:", n+m)
    print("tru:", n-m)
    print("nhan:", n*m)
    if n!=0 and m!=0:
        print("chia", n/m)
    else:
        print(" hu cau")
    print("luy thua:",n**m)
    if n>=0:
        print("can cua n:",math.sqrt(n))
    else:
        print("hu cau")
    if m>=0:
        print("can cua m:",math.sqrt(m))
    else:
        print("hu cau")
    a=input("ban muon tiep tuc khong? c/k")
    if a.lower() != 'c':
        break
#6

    

        
