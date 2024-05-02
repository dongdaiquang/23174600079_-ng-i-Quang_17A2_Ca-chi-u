#lab7
#1
N=int(input("nhap so nguyen"))
Quang_dict={x: x**3 for x in range(1, N+1)}
for key, value in Quang_dict.items():
    print(f"{key}; {value}")
#2
danh_sach={}
for i in range(1,11):
    name=input("ten sinh vien:")
    diem=float(input("diem thi:"))
    danh_sach[name]=diem
bang_diem={'A': 0, 'B':0, 'C':0, 'D':0, 'F':0}
for name, diem in danh_sach.items():
    if diem>=8.5:
        bang_diem['A']+=1
    elif diem>=7.0:
        bang_diem['B']+=1
    elif diem>=5.5:
        bang_diem['C']+=1
    elif diem>=4.0:
        bang_diem['D']+=1
    else:
        bang_diem['F']+=1
print(" xep laoi hoc luc cua sinh vien")
for name, diem in danh_sach.items():
    if diem >=8.5:
        print(f"{name}:A")
    elif diem >=7.0:
        print(f"{name}:B")
    elif diem >=5.5:
        print(f"{name}:C")
    elif diem >=4.0:
        print(f"{name}:D")
    else:
        print(f"{name}:F")
for y, x in bang_diem.items():
    print(f"{y}: {x} sinh vien")
#3
text = "Dog is a pet animal. It is the oldest friend of human beings. It watches our house. It is very faithful animal and never left his master. It is used by police to fight crime. Sheep-rearers also use them. Thus it is useful for us in many ways."
tu_dien={}
for i in text.lower().split():
    i=i.strip(".,!")
    if i in tu_dien:
        tu_dien[i]+=1
    else:
        tu_dien[i]=1
Max=max(tu_dien,key=tu_dien.get)
Min=min(tu_dien,key=tu_dien.get)
for i, x in tu_dien.items():
    print(f"{i}: {x}")
print("tu xuat hien nhieu nhat", Max, "voi so lan xuat hien",tu_dien[Max])
print("tu xuat hien it nhat", Min, "voi so lan xuat hien",tu_dien[Min])
#4
inventory = {
'gold' : 500,
'pouch' : ['flint', 'twine', 'gemstone'],
'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']

}
inventory['pocket']=['seashell','strange berry','lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold']=50
print(inventory)
    
    
