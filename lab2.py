#lab2
#1
a=int(input("nhap vao a"))
b=int(input("nhap vao b"))
if a==0:
    if b==0:
        print("vo so nghiem")
    else:
        print("vo nghiem")
else:
    x=-b/a
    print("x=", x)
#2
so=str(input("nhap so"))
if len(so)<4:
    print("0")
else:
    lay_hang_nghin=int(so[0])
    print("chu so hang nghin", lay_hang_nghin)
#3
n=int(input("Nhap vao so nguyen n:"))
if 100<=n <= 999:
    chu_so_hang_tram = n // 100
    chu_so_hang_chuc = (n//10) % 10
    chu_so_hang_don_vi = n % 10
    if chu_so_hang_tram == 1:
        doc_hang_tram = "one hundred"
    elif chu_so_hang_tram == 2:
        doc_hang_tram = 'two hundred'
    elif chu_so_hang_tram == 3:
        doc_hang_tram = 'three hundred'
    elif chu_so_hang_tram == 4:
        doc_hang_tram = 'four hundred'
    elif chu_so_hang_tram == 5:
        doc_hang_tram = 'five hundred'
    elif chu_so_hang_tram == 6:
        doc_hang_tram = 'six hundred'
    elif chu_so_hang_tram == 7:
        doc_hang_tram = 'seven hundred'
    elif chu_so_hang_tram == 8:
        doc_hang_tram = 'eight hundred'
    elif chu_so_hang_tram == 9:
        doc_hang_tram = 'nice hundred'
    elif chu_so_hang_tram == 0:
        doc_hang_tram = ''
    if chu_so_hang_chuc == 1:
        doc_hang_chuc = "ten"
    elif chu_so_hang_chuc == 2:
        doc_hang_chuc = 'twenty'
    elif chu_so_hang_chuc == 3:
        doc_hang_chuc = 'thỉrty'
    elif chu_so_hang_chuc == 4:
        doc_hang_chuc = 'forty'
    elif chu_so_hang_chuc == 5:
        doc_hang_chuc = 'fifty'
    elif chu_so_hang_chuc == 6:
        doc_hang_chuc = 'sixty'
    elif chu_so_hang_chuc == 7:
        doc_hang_chuc = 'bảy mươi'
    elif chu_so_hang_chuc == 8:
        doc_hang_chuc = 'seventies'
    elif chu_so_hang_chuc == 9:
        doc_hang_chuc = 'nicety'
    elif chu_so_hang_chuc == 0:
        doc_hang_chuc = 'zero'
    if chu_so_hang_don_vi == 1:
        doc_hang_don_vi = "onee"
    elif chu_so_hang_don_vi == 2:
        doc_hang_don_vi = 'two'
    elif chu_so_hang_don_vi == 3:
        doc_hang_don_vi = 'three'
    elif chu_so_hang_don_vi == 4:
        doc_hang_don_vi = 'four'
    elif chu_so_hang_don_vi == 5:
        doc_hang_don_vi = 'five'
    elif chu_so_hang_don_vi == 6:
        doc_hang_don_vi = 'six'
    elif chu_so_hang_don_vi == 7:
        doc_hang_don_vi = 'sevev'
    elif chu_so_hang_don_vi == 8:
        doc_hang_don_vi = 'eight'
    elif chu_so_hang_don_vi == 9:
        doc_hang_don_vi = 'nice'
    elif chu_so_hang_don_vi == 0:
        doc_hang_don_vi = ''
    print("Số",n, "đọc là:", doc_hang_tram, doc_hang_chuc, doc_hang_don_vi)
#4
diem_so=float(input("nhap diem so"))
if diem_so>0:
    if 0<= diem_so<=5:
        print("diem kem")
    elif 5< diem_so<+7:
        print("diem trung binh")
    elif 7< diem_so<=8.5:
        print("diem kha")
    elif 8.5< diem_so<=10:
        print("diem gioi")
else:
    print("khong hop le")
#5
n=int(input("nhap so nguoi"))
gia_ve_mot_nguoi=120000
tong_tien=n*gia_ve_mot_nguoi
if n>0:
    if 2<=n<=4:
        tong_tien*=0.95
        print("tong tien", tong_tien)
    elif 4<n<=10:
        tong_tien*=0.9
        print("tong tien", tong_tien)
    elif n>10:
        tong_tien*=0.8
        print("tong tien", tong_tien)
else:
    print("khong hop le")
#6
a=int(input("nhap so a"))
b=int(input("nhap so b"))
c=int(input("nhap so c"))
if a>=0 or b>=0 or c>=0:
    if a>=b>=c or c>=b>=a:
        print("so lon thu 2", b)
    elif b>=a>=c or c>=a>=b:
        print("so lon thu 2", a)
    else:
        print("so lon thu 2", c)
else:
    print("khong hop le")
#7
can_nang=float(input("nhap can nang"))
chieu_cao=float(input("nhap chieu cao"))
bmi=can_nang/(chieu_cao**2)
if bmi<18.5:
    print("gay")
elif 18.5<=bmi<=25.0:
    print("binh thuong")
elif 25.0<=bmi<=30.0:
    print("hoi beo")
else:
    print("beo")
#8
he_so_goc_1=float(input("nhap he so goc canh 1"))
he_so_tu_do_1=float(input("nhap he so tu do canh 1"))
he_so_goc_2=float(input("nhap he so goc canh 2"))
he_so_tu_do_2=float(input("nhap he so tu do canh 2"))
if he_so_goc_1==he_so_goc_2 and he_so_tu_do_1!=he_so_tu_do_2:
    print("hai duong thang song song")
elif he_so_goc_1*he_so_goc_2==-1:
    print("hai dương thang vuong goc")
else:
    print("hai duong thang cat nhau")
#9
import math
a=float(input("nhap he so goc cua duong tb"))
b=float(input("nhap he so tu do cua duong thang"))
x=float(input("nhap toa do x cua tam"))
y=float(input("nhap toa do y cua tam"))
ban_kinh=float(input("nhap ban kinh"))
c=abs(y-(a*x +b))/math.sqrt(a**2+1)
if c< ban_kinh:
    print("duong thang cat duong tron")
elif c== ban_kinh:
    print("duong thang tiep xuc duong tron")
else:
    print("duong thang nam ngoai duong tron")
    


