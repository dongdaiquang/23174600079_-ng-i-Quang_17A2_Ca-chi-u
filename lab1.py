#1
print("""
i carry your heart with me (i carry it in
my heart) i am never without it (anywhere
i go you go, my dear; and whatever is done
by only me is your doing, my darling)
i fear no fate (for you are my fate, my sweet)
i want no world (for beautiful you are my world, my true)
and it's you are whatever a moon has always meant
and whatever a sun will always sing is you

here is the deepest secret nobody knows
(here is the root of the root and the bud of the bud
and the sky of the sky of a tree called life; which grows
higher than soul can hope or mind can hide)
and this is the wonder that's keeping the stars apart

i carry your heart (i carry it in my heart)
---i carry your heart with me by e.e. cummings---
""")
#2
ma_sach=int(input("nhap ma sach"))
ten_sach=input("nhap ma sach")
tac_gia=input("nhap ten tac gia")
so_luong=float(input("nhap so luong"))
print('Thong tin sinh vien:')
print(f'tac gia:{tac_gia}')
print(f'ten sach:{ten_sach}')
print(f'so_luong:{so_luong}')
#3
tien_ban_dau=10000
lai_suat_nam=0.06
amount_after_5_years=tien_ban_dau*(1+lai_suat_nam)**5
amount_after_10_years=tien_ban_dau*(1+lai_suat_nam)**10
ty_le_tang_truong=(amount_after_10_years-amount_after_5_years)/amount_after_5_years
print("Số tiền sau 5 năm là:", round(amount_after_5_years, 2))
print("Số tiền sau 10 năm là:", round(amount_after_10_years, 2))
print("Tỷ lệ tăng trưởng sau 10 năm so với 5 năm là:", round(ty_le_tang_truong * 100, 2), "%")
#4
import math
canh_day=float(input("nhap do dai canh day"))
chieu_cao=float(input("nhap chieu cao hinh chop"))
dien_tich_xung_quanh=4*1/2*canh_day*chieu_cao
dien_tich_day=canh_day**2
dien_tich_toan_phan=dien_tich_xung_quanh+dien_tich_day
the_tich=1/3 *dien_tich_day* chieu_cao
print("dien tich xung quanh", dien_tich_xung_quanh)
print("dien tich toan_phan", dien_tich_toan_phan)
print("the tich", the_tich)
#5
gia_dien = 5000
dien_ap = 220
cuong_do_dien = 1.5
cong_suat = dien_ap * cuong_do_dien
so_gio_su_dung = float(input("Nhập số giờ sử dụng máy lọc không khí: "))
so_kWh_su_dung = (cong_suat / 1000) * so_gio_su_dung
tong_tien_dien = so_kWh_su_dung * gia_dien
print("Tổng số tiền điện phải trả cho việc sử dụng máy lọc không khí là:", round(tong_tien_dien, 2), "đồng")
#6
import math
a0=int(input("nhap so hoanh do a"))
a1=int(input("nhap so tung do a"))
b0=int(input("nhap so hoanh do b"))
b1=int(input("nhap so tung do b"))
g_x=a0 + b0
g_y=a1 + b1
g_x1=a0-b0
g_y1=a1-b1
c=math.sqrt(a0**2 + a1**2)
d=math.sqrt(b0**2 + b1**2)
cosin=(a0*b0+a1*b1)/c*d
print("tong vecto a+b la", g_x, ",", g_y)
print("hieu vecto a-b la", g_x1,",", g_y1)
print("do dai vecto a", c)
print("do dai vecto b", d)
print("cosin goc hop boi 2 vecto a va b", cosin)
#7
import math
a1=float(input("nhap a1"))
a2=float(input("nhap a2"))
b1=float(input("nhap b1"))
b2=float(input("nhap b2"))
c1=float(input("nhap c1"))
c2=float(input("nhap c2"))
dinh_luong=a1*b2-a2*b1
x=(c1*b2-c2*b1)/dinh_luong
y=(c2*a1-c1*a2)/dinh_luong
print("nghiem x:", x)
print("nghiem y:", y)
#8
import math
x=float(input("nhap x:"))
z=float(input("nhap z:"))
f=((math.sin(z))*x**2 +(abs(x)**1/2))/((math.log(z))+2.7**(x-1))
print("giá trị của f:", f)
#9
x1=float(input("nhap hoanh do M"))
y1=float(input("nhap tung do M"))
x2=float(input("nhap hoanh do N"))
y2=float(input("nhap tung do N"))
x3=float(input("nhap hoanh do P"))
y3=float(input("nhap tung do P"))
x4=float(input("nhap hoanh do Q"))
y4=float(input("nhap tung do Q"))
a=(x1+x2)/2
a1=(y1+y2)/2
b=(x2+x3)/2
b1=(y2+y3)/2
c=(x3+x4)/2
c1=(y3+y4)/2
d=(x1+x4)/2
d1=(y1+y4)/2
print("toa do trung diem cua MN", a,",", a1)
print("toa do trung dien cua NP", b,",", b1)
print("toa do trung diem cua PQ", c,",", c1)
print("toa do trung diem cua QM", d,",", d1)




























































































































































































































