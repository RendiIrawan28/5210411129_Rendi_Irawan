#class Buku
class Buku:
    def __init__(self,judul,pengarang,tahun_terbit):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit

buku = Buku("Tenggelamnya Kapal Van der Wijck", "HAMKA", 1938)
# # Menambahkan dua objek pada classBuku
cerpen = Buku("Si Pahit Lidah","santoso", 2000)
novel = Buku("Putri Malu","jauhari",1980)
list_buku = [buku, cerpen, novel]
print("##### Daftar Buku #####","\n")
for x in list_buku:
    t = "Buku {} karangan {} pertama kali diterbitkan tahun {}".format(x.judul,x.pengarang,x.tahun_terbit)
    print(t)



#Class Mahasiswa
class Mahasiswa:
    def __init__(self,nama,nim,prodi,thn_masuk):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.thn_masuk =thn_masuk

m1 = Mahasiswa ("Udin","10120371","Sistem Informasi",2020)
# Menambahkan dua objek pada ClassMahasiswa
m2 = Mahasiswa ("Rendi Irawan","5210411129","Informatika",2021)
m3 = Mahasiswa ("Arel","5170043111","Teknik Komputer",2017)
daftar_mahasiswa =[m1,m2,m3]
print("***** Daftar Mahasiswa *****","\n")
for y in daftar_mahasiswa:
    teks ="{} adalah mahasiswa {} angkatan {} dengan nim {}".format(y.nama,y.prodi,y.thn_masuk,y.nim)
    print(teks)


# #ClassMinuman
class MenuMinuman:
    def __init__(self,nama,deskripsi,harga):
        self.nama = nama
        self.deskripsi = deskripsi 
        self.harga = harga

mnm1 = MenuMinuman("Jus jambu","Jus jambu merah tanpa gula",8500)
mnm2 = MenuMinuman("Jus alpukat Ori","Jus alpukat dengan tambahan air gula merah", 1500) 
mnm3 = MenuMinuman("Jus alpukat xtra milk","Jus alpukat dengan campuran susu coklat dan taburankeping choco", 15000)
mnm4 = MenuMinuman("Red & Smooth","Smoothie pisang susu dengan strawberry",17500)
# Menambahkan dua objek pada class MenuMinuman
mnm5 = MenuMinuman("Es mangga coklat","es mangga yang dicampur coklat",8000)
mnm6 = MenuMinuman("Es degan"," Es kelapa muda dengan susu",5000)

pilihan_minuman =[mnm1,mnm2,mnm3,mnm4,mnm5,mnm6]
print("Daftar menu Health Fruits")
for mn in pilihan_minuman:
    t = "{} Harga Rp {}, {}".format(mn.nama,mn.harga,mn.deskripsi)
    print(t)