#lab8
#1
def so_nguyen_to(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def so_sinh_doi(x):
    m=[]
    for num in range(2,x):
        if so_nguyen_to(num):
            m.append(num)
    sinh_doi=[]
    for i in range(len(m)-1):
        if m[i+1]-m[i]==2:
            sinh_doi.append((m[i], m[i+1]))
    return sinh_doi
x=1000
sinh_doi=so_sinh_doi(x)
for w in sinh_doi:
    print(w)
#2
def factorial(n):
    if n==0 or n==1:
        return 1
    result=1
    for i in range(2,n+1):
        result*=i
    return result
def hoan_vi(n,r):
    return factorial(n)//factorial(n-r)
def to_hop(n,r):
    return hoan_vi(n,r)//factorial(r)
n=int(input("nhap n phan tu"))
r=int(input("nhap r phan tu"))
print(f"Số hoán vị của {n} phần tử lấy {r} phần tử mỗi lần: p({n}, {r}) = {hoan_vi(n, r)}")
print(f"Số tổ hợp của {n} phần tử lấy {r} phần tử mỗi lần: c({n}, {r}) = {to_hop(n, r)}")
#3
def cubesum(n):
    sum=0
    while n>0:
        m=n%10
        sum+=m**3
        n//=10
    return sum
def PrintArmstrong():
    for num in range(1000):
        if num==cubesum(num):
            print(num)
def isArmstrong(n):
    return n==cubesum(n)
print("Các số Armstrong trong khoảng từ 0 đến 999 là:")
PrintArmstrong()
n=int(input("nhap so:"))
if isArmstrong(n):
    print(f"{n} la so Armstrong")
else:
    print(f"{n} khong phai la so Armstrong")
#4
def sumPdivisors(n):
    tong_uoc=0
    for i in range(1,n):
        if n%i==0:
            tong_uoc+=i
    return tong_uoc
n=int(input("nhap n:"))
print(f"tong uoc so chinh phương cua {n} la: {sumPdivisors(n)}")
#5
def sumPdivisors(n):
    tong_uoc=0
    for i in range(1,n):
        if n%i==0:
            tong_uoc+=i
    return tong_uoc
def amicable(a,b):
    return a!=b and sumPdivisors(a)==b and sumPdivisors(b)==a
a=int(input("nhap so thu 1:"))
b=int(input("nhap so thu 2:"))
if amicable(a,b):
    print(f"{a} va {b} la cap so amicable")
else:
    print(f"{a} va {b} khong la cap amicable")
#6
#a
def loc_so_le(n):
    return list(filter(lambda x: x%2 !=0,n))
n=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
m=loc_so_le(n)
print("cac so le",m)
#b
def loc_so_chan(n):
    return list(filter(lambda x: x%2 ==0,n))
n=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
m=loc_so_chan(n)
print("cac so chan",m)
#c
def lap_phuong(n):
    return list(map(lambda x: x**3,n))
n=[1, 2, 3, 4, 5]
m=lap_phuong(n)
print("lap_phuong",m)
#d
def lap_phuong_chan(n):
    so_chan=filter(lambda x: x%2 ==0,n)
    return list(map(lambda x: x**3, so_chan))
n=[1, 2, 3, 4, 5]
m=lap_phuong_chan(n)
print("lap phuong chan", m)


    
        
