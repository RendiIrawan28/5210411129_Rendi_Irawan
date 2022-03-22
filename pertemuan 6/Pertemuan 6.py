#polymorphism dengan fungsi

print(len('Polymorphism'))
print(len([0,1,2,3]))

'''
Menggunakan Fungsi len
Output :
12 (Tipe Data String)
4 (Tipe Data List)
'''

#using class
class jerman:
    def ibukota(self):
        print('Berlin adalah ibukota negara Jerman')

class jepang:
    def ibukota(self):
        print('Tokyo adalah ibukota Jepang')

negara1 = jerman()
negara2 = jepang()

for country in (negara1,negara2):
    country.ibukota()




print('#'*60)





#implementasi Overloading

class Pegawai:
    jumlah = 0

    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji
        Pegawai.jumlah +=1

    def tampilJumlah(self):
        print('Total pegawai', Pegawai.jumlah)
    
    def tampilPegawai(self):
        print('Nama : ',self.nama,' gaji : ', self.gaji)

    #method overloading
    def tunjangan(self,istri=None,anak=None):
        if anak != None and istri != None:
            total = anak+istri
            print('Tunjangan Anak + Istri = ',total)


# memanggil class
peg1 = Pegawai('Eren',2000)
peg2 = Pegawai('Lutfi',6000)
peg1.tampilPegawai()
peg2.tampilPegawai()
peg1.tunjangan(2500,2000)
peg2.tunjangan(2500,3000)

print('Total pegawai %d'% Pegawai.jumlah)
rataGaji = (peg1.gaji + peg2.gaji)/Pegawai.jumlah
print('Rata-rata gaji = '+str(rataGaji))




print('#'*60)



#Overriding Segiempat
class Segiempat():
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitungLuas(self): #method Overriding
        print('luas segiempat = ',self.panjang*self.lebar, 'm^2')

class Bujursangkar(Segiempat):
    def __init__(self,sisi):
        self.side = sisi
        Segiempat.__init__(self,sisi,sisi)

    def hitungLuas(self): #method Overriding
        print('Luas Bujur sangkar = ', self.side*self.side,'m^2')

b=Bujursangkar(4)
s=Segiempat(2,4)
b.hitungLuas()
s.hitungLuas()




print('#'*60)



#Overloading Mahasiswa
class Mahasiswa:
    def __init__(self,nama,nim):
        self.nama = nama
        self.nim = nim
        #self.prodi = prodi
        #self.thn_masuk = thn_masuk
        #self.semester = semester

    def tampilMhs(self):
        print('nama : ',self.nama,', Nim : ',self.nim)

    #method Overloading
    def hitungSKS(self,jmlsks = None , sks = None):
        if jmlsks != None and sks != None:
            totalsks = jmlsks+sks
            print('Total sks = ', totalsks)

        else:
            totalsks = jmlsks
            print('Total sks = ',totalsks)


mhs1 = Mahasiswa('Eren',123180015)
mhs2 = Mahasiswa('Luffy',123190007)
mhs1.tampilMhs()
mhs2.tampilMhs()
mhs1.hitungSKS(80,34)
mhs2.hitungSKS(83)





print('#'*60)




#Overriding Mahasiswa
class Mahasiswa():   
    def __init__(self,nama,nim):
        self.nama = nama #Atribut Public
        self.nim = nim #Atribut Public
    
    def detSiswa(self):
        print(self.nama, "alamat : Wall Rose") #cetak data dengan panggil atribut publik nama

class Siswa(Mahasiswa):
    def __init__(self,jurusan,nim):
        self.jurusan = jurusan #Atribut Public
        self.nim = nim #Atribut Public

    def detSiswa(self):
        print(self.jurusan,"Jurusan : Informatika") #cetak data dengan panggil atribut publik jurusan

#Membuat objek
mhs1 = Siswa("Mikasa", 135105)
mhs2 = Mahasiswa("Nezuko", 135119)

print(mhs1.nim, mhs2.nama) #cetak data
mhs1.detSiswa() 
print(mhs1.nim, mhs2.nama) 
mhs2.detSiswa() 






print('#'*60)





# Polymorphism dengan class
class Kucing:
    def __init__(self, nama, umur):
        self.nama = nama #Atribut Public
        self.umur = umur 

    
    def bersuara(self): #Function bersuara
        print("Meow") # cetak

class Dog():
    def __init__(self, nama, umur):
        self.nama = nama #Atribut Public
        self.umur = umur

    def bersuara(self):
        print("Guk..guk..") #Cetak

#Mebyuat objek dsimpan dalam sebuah variabel
kucing1 = Kucing("Tom", 3) #Variabel 1
anjing1 = Dog("Spike", 4) #Variabel w2

#Menggunakan perulangn for yang menyimpan variabel  kucing1 dan anjing1
for hewan in (kucing1, anjing1): 
    hewan.bersuara()






print('#'*60)





#Polymorhism Inheritance

class Burung:
    def intro(self): #Fungction intro menyimpan parameter self
        print("Di dunia ini ada beberapa type berbeda dari spesies burung") # Cetak

    def terbang(self): #Fungtion terbang menyimpan parameter self
        print("Hampir semua burung dapat terbang, namun ada beberapa yang tidak dapat terbang") #Cetak

class Elang(Burung): #Class Elang dengan menyimpan atau merujuk pada class Burung
    def terbang(self):
        print("Elang dapat terbang") #Cetak

class BurungUnta(Burung):
    def terbang(self): #Fungction terbang menyimpan parameter self
        print("Burung unta tidak dapat terbang")
# Dibuat permisalan dengan variabel untuk setiap class
obj_burung = Burung()
obj_elang = Elang()
obj_burung_unta = BurungUnta()

obj_burung.intro() 

#Panggil class
obj_elang.intro() 
obj_elang.terbang() 

obj_burung_unta.intro() 
obj_burung_unta.terbang()