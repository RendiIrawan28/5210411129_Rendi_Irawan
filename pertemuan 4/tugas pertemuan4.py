#Class Buku (nama kelass)
class Buku:
    def __init__(self,judul,pengarang,tahun_terbit,penerbit_buku): #membuat variabel
        self.judul = judul 
        self.pengarang = pengarang 
        self.tahun_terbit = tahun_terbit 
        #Menambahkan atribut Private
        self.__penerbit_buku = penerbit_buku
buku = Buku("Tenggelamnya Kapal Van der Wijck", "HAMKA", 1938,"Centrale Courant") #variabel untuk menampung data
cerpen = Buku("Si Pahit Lidah","santoso", 2000,'merdeka pustaka') #variabel 2
novel = Buku("Putri Malu","jauhari",1980,'media dulu')#variabel 3
list_buku = [buku, cerpen, novel]
print("***** Daftar Buku *****","\n")
for x in list_buku:
    t = "Buku {} karangan {} pertama kali diterbitkan tahun {} yang diterbitkan oleh {} ".format(x.judul,x.pengarang,x.tahun_terbit,x._Buku__penerbit_buku)
    print(t)#untuk menampilkan






#nama class mahasiswa
class Mahasiswa: 
    def __init__(self,nama,nim,prodi,thn_masuk,daerah):
        self.nama = nama 
        self.nim = nim 
        self.prodi = prodi
        self.thn_masuk =thn_masuk
        #Menambahkan atribut private
        self.__daerah= daerah

m1 = Mahasiswa ("Udin","10120371","Sistem Informasi",2020,"Jepara") 
m2 = Mahasiswa ("Rendi Irawan","5210411129","Informatika",2021,'lampung Timur')
m3 = Mahasiswa ("Arel","5170043111","Teknik Komputer",2017,'medan')

daftar_mahasiswa =[m1,m2,m3]
print("***** Daftar Mahasiswa *****","\n")
for y in daftar_mahasiswa: 
    teks ="{} adalah mahasiswa {} angkatan {} dengan nim {} asal daerah {}".format(y.nama,y.prodi,y.thn_masuk,y.nim,y._Mahasiswa__daerah)
    print(teks)









class MenuMinuman: 
    def __init__(self,nama,deskripsi,harga,jumlah): 
        self.nama = nama
        self.deskripsi = deskripsi 
        self.harga = harga
        self.__jumlah = jumlah 

mnm1 = MenuMinuman("Jus jambu","Jus jambu merah tanpa gula",8500, 3) 
mnm2 = MenuMinuman("Jus alpukat Ori","Jus alpukat dengan tambahan air gula merah", 1500, 1) 
mnm3 = MenuMinuman("Jus alpukat xtra milk","Jus alpukat dengan campuran susu coklat dan taburankeping choco", 15000, 2)
mnm4 = MenuMinuman("Red & Smooth","Smoothie pisang susu dengan strawberry",17500, 1) 
# Menambahkan dua objek pada class MenuMinuman
mnm5 = MenuMinuman("Es mangga coklat","es mangga yang dicampur coklat",8000,4)
mnm6 = MenuMinuman("Es degan"," Es kelapa muda dengan susu",5000,7)


pilihan_minuman =[mnm1,mnm2,mnm3,mnm4,mnm5,mnm6]
print("Daftar menu Health Fruits")  
for mn in pilihan_minuman: 
    t = "{} Harga Rp {}, {} {} porsi".format(mn.nama,mn.harga,mn.deskripsi,mn._MenuMinuman__jumlah)
    print(t)