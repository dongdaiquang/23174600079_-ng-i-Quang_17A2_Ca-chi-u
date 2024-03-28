#lab3
#1
#a
n=int(input("nhap so n:"))
tong=0
if n<=0:
    print("nhap lai so")
else:
    for i in range(1,n+1):
        tong+=i
    print("S1=", tong)
#b
n=int(input("nhap so n:"))
tong=0
if n<=0:
    print("nhap lai so")
else:
    for i in range(1,n+1):
        tong+=1/i
    print("S2=", tong)
#c
import math
n=int(input("nhap so n:"))
tong=0
if n<=0:
    print("nhap lai so")
else:
    for i in range(1,n+1):
        tong+=1/math.sqrt(2*i)
    print("S3=", tong)
#d
n=int(input("nhap so n:"))
tong=0
if n<=0:
    print("nhap lai so")
else:
    for i in range(1,n+1):
        tong+=(-1)**(i+1)/i
    print("S4=", tong)
#2
#a
tong=0
for i in range(2000,4001):
    if i%7==0 and i%4!=0:
        tong+=i
print("tong cac so chia het cho 7 và khong chia het cho 5", tong)
#b
tong=0
for i in range(500,1001):
    if i%4==0 and i%6!=0:
        tong+=i
print("tong cac so chia het cho 4 và khong chia het cho 6 ", tong)
#3
#a
for num in range(100,1001):
    if num>1:
        prime=True
        for i in range(2,num):
            if num%i==0:
                prime=False
                break
        if prime:
            print(num, end=" ")
#b
for i in range(1,1001):
    if i==int(i**0.5)**2:
        print(i)
#c
f0=0;
f1=1;
fn=1;
for i in range(1,100):
    f0=f1;
    f1=fn;
    fn=f0+f1;
print(fn)
#d
for num in range(2,500):
    tong=0
    for i in range(1,num):
        if num%i==0:
            tong+=i
    if tong==num:
        print(num)
        
#4
#a
for i in range(1, 6):
    for j in range(5-i):
        print(' ',end ='')
    for j in range(i):
        print("* ", end ='')
    print()
for i in range(5,0,-1):
    for j in range(5-i):
        print(' ',end ='')
    for j in range(i):
        print("* ", end ='')
    print()
#b
for i in range(7):
    print(" " * (7 - i - 1), end="")
    print("*" * (2 * i + 1))
print()        
for i in range(4):
    if i == 4 // 2:
            print(" " * ((13 - 3) // 2) + "*" * 3 + " " * ((13 - 3) // 2))
    else:
            print(" " * (13 // 2 - 3 // 2) + "*" * 3 + " " * (13 // 2 - 3 // 2))
print()
                
        
    
