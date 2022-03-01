
a ='aku cinta indonesia'
print (a)
a=a[:10]+'tanah air ku'+a[9:]
print (a)

a =''
print(a)

str1 = 'aku cinta tanah air ku indonesia'
str1 = str1[:9]+''+str1[22:]
print(str1)

kelas='Praktikum Pemrograman Berorientasi Objek'
besar= kelas.upper()
kecil= kelas.lower()
print(kelas)
print(besar)
print(len(kelas))

s="     Python     "
print(s.strip())
print(s.lstrip())
print(s.rstrip())

s1 = 'Python '
s2 = 'Programing'
s3 = s1+s2
print(s3)

kelas2 = kelas.replace('Praktikum','Praktik')
print(kelas2)

x='1'
y='2'
z='3'
print('saya punya mangga %s dirumah'%(y))

coba = input("hari ini adalah : ")
print (coba)

masuk1= input("masukan angka 1 : ")
masuk2= input("masukan angka 2 : ")
hasil = int(masuk1)*int(masuk2)
print (masuk1,'*',masuk2,'=',hasil)

List = [0,1,2,3,4,5,6,7,8,9]
print (List)
print(List[5])
print(List[:3])
print(len(List))
print(List[10-3:])
print(List[2:9])

List.append(10)
print(List)

List.insert(1,11)
print(List)

List2 = ('halo')
List.extend(List2)
print(List)

List.extend('hai')
print(List)

del List[1]
print (List)

List.remove(10)
print(List)

List.pop()
print(List)

List.pop(2)
print(List)

b = [50,10,20,30,40]
c = sorted(b)
print (c)

b.sort()
print (b)

b.sort(reverse=True)
print(b)

min(b)
print(b)

max(b)
print(b)

d = {1:100,2:200,3:300,4:400,5:500}
print(d)

d.get(2)
print(d)

d.get(4)
print(d)

d.keys()
print(d)

d.values()
print(d)

del d[1]
print (d)

d.clear()
print(d)


t=(100,200,300,400)
print(t)

t.index(200)
print(t)

a1=[10,15,20,25,30,35,40,45,50]
b1 = set (a1)



