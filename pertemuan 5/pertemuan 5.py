# Hierachical Inheritance

#class parent atau class induk
class Induk:
    def fungsiinduk(self): #
        print("Fungsi pada parent class")#cetak

#class turunan 1
class Anak1(Induk): 
    def fungsianak1(self):
        print("Fungsi pada anak 1.") #cetak

#class turunan 2
class Anak2(Induk): 
    def fungsianak2(self): 
        print("Fungsi pada anak 2.") #cetak

a1 = Anak1() 
a2 = Anak2() 

a1.fungsiinduk()
a1.fungsianak1() 

a2.fungsianak2()







# Hierachical Inheritance  class mahasiswa

#Class mahasiswwa
class Mahasiswa: 
    def __init__(self,nama,nim): 
        self.nama = nama 
        self.nim = nim 

class Siswa1(Mahasiswa):
    def __init__(self,nama,nim): 
        self.nama = nama 
        self.nim = nim 

    def detSiswa1(self): 
        print (self.nama, "alamat : Wall rose")

class Siswa2 (Mahasiswa): 
    def __init__(self,nama,nim): 
        self.nama = nama 
        self.nim = nim 
        
    def detSiswa2(self):  
        print(self.nama, "Jurusan : Informatika") 
#Membuat objek mhs1 dan mhs2
mhs1 = Siswa1 ("Mikasa", 135105)
mhs2 = Siswa2 ("Nezuko", 1351117)

print(mhs1.nim) 
mhs1.detSiswa1() 
print(mhs2.nim) 
mhs2.detSiswa2()






#Multilevel Inheritance

#Parent Class hewan
class Hewan : 
    def bersuara(self): 
        print("Kucing bersuara") 

#Child class mewarisi class hewan
class Kucing(Hewan): 
    def suara(self): 
        print("meong...meong...meong") 
#Child class mewarisi dari class Hewan
class AnakKucing(Kucing):
    def minum(self):
        print("Minum susu")

#objek
ak = AnakKucing() 
ak.bersuara() 
ak.suara()
ak.minum()






#Multilevel Inheritance class mahasiswa

class Mahasiswa:
    def __init__(self,nama,nim): 
        self.nama = nama 
        self.nim = nim 

class Siswa1(Mahasiswa): 
    def __init__(self,nama,nim): 
        self.nama = nama
        self.nim = nim 

class Siswa2(Siswa1): 
    def __init__(self,nama,nim):
        self.nama = nama 
        self.nim = nim 

#Membuat objek mhs1, mhs2, mhs3
mhs1 = Mahasiswa("Mikasa", 135105)
mhs2 = Siswa1 ("Nezuko", 135117)
mhs3 = Siswa2 ("Hancock", 134079)

#Cetak data
print(mhs1.nama, mhs1.nim)
print(mhs2.nim)
print(mhs3.nama)








# Multiple Inheritance

class Perhitungan1: 
    def penjumlahan(self,a,b): 
        return a+b 

#Parent 2
class Perhitungan2:#Class perhitungan2
    def perkalian(self,a,b):
        return a*b 

# Child

class Hitung(Perhitungan1, Perhitungan2):
    def pembagian(self,a,b): 
        return a/b 

#Membuat objek
h= Hitung() 
print("Penjumlahan : ",h.penjumlahan(20,30)) 
print("Perkalian : ",h.perkalian(2,4)) 
print("Pembagian : ",h.pembagian(6,12)) 









# Multiple Inheritance Mahasiswa1

class Mahasiswa1(): 
    def __init__(self,nama,nim): 
        self.nim = nim 
        self.nama = nama

class Mahasiswa2():
    def __init__(self,alamat,jurusan):
        self.alamat = alamat 
        self.jurusan = jurusan 

class Siswa(Mahasiswa1,Mahasiswa2): 
    def __init__(self,nim,nama,alamat,jurusan):
        Mahasiswa1.__init__(self,nama,nim)
        Mahasiswa2.__init__(self,alamat,jurusan)
print()
#Membuat objek
s = Siswa("Mikasa", 135105,"Wall rose","Informatika")
print("Nim : ",s.nim, "Nama : ",s.nama, "Alamat : ",s.alamat,"Jurusan : ",s.jurusan) 








# Single Inheritance

class Hewan : 
    def bersuara(self): 
        print("Kucing bersuara") 

#Child Class mewarsi class Hewan
class Kucing(Hewan): 
    def Suara(self): 
        print("meong...meong...,meong") 

#Menambahkan objek
k = Kucing() 
k.Suara() 
k.bersuara() 








#Single inheritance

class Mahasiswa:
    def __init__(self,nama,nim):
        self.nama = nama
        self.nim = nim
    
    def detailMhs(self): 
        return self.nim, self.nama 
    
    def CekMhs(self): 
        if self.nim <150000:
            return "Mahasiswa Aktif" 
        else: 
            return "Mahasiswa tidak terdaftar "

class Siswa(Mahasiswa):
    def End(self):
        print(" Mahasiswa belum melakukan daftar ulang") 
# Objek 1
mahasiswa1 = Mahasiswa("Mahasiswa 1", 135103)
print(mahasiswa1.detailMhs(), mahasiswa1.CekMhs()) 
# Objek 2
mahasiswa2 = Siswa ("Mahasiwa 2", 150503)
print(mahasiswa2.detailMhs(), mahasiswa2.CekMhs()) 
mahasiswa2.End()








class ComputerPart(): 
    def __init__ (self,pabrikan,nama,jenis,harga):
        self.pabrikan = pabrikan 
        self.nama = nama 
        self.jenis = jenis 
        self.harga = harga 

class Processor(ComputerPart):
    def __init__(self,pabrikan,nama,harga,jumlah_core,speed):
       
        super().__init__(pabrikan,nama,"Processor",harga)
        self.jumlah_core = jumlah_core
        self.speed = speed 

class RandomAccessMemory(ComputerPart):
    def __init__(self,pabrikan,nama,harga,kapasitas):
        
        super().__init__(pabrikan,nama,"RAM",harga)
        self.kapasitas = kapasitas 

class HardDiskSATA(ComputerPart):
    def __init__(self,pabrikan,nama,harga,kapasitas,rpm):
        super().__init__(pabrikan,nama,"SATA",harga)
        self.kapasitas = kapasitas 
        self.rpm = rpm 
#Membuat objek
p = Processor("Intel","Core i7 7740X",4350000,4," 4.3GHZ")
m = RandomAccessMemory("V-Gen", "DDR4 SODimm PC19200/2400MHZ",328000,"4GB")
hdd = HardDiskSATA("Seagate","HDD 2.5 inch",295000,"5000GB",7200)

parts = [p,m,hdd] 
for part in parts: 
    print ("{} {} produksi {}".format(part.jenis,part.nama,part.pabrikan)) 