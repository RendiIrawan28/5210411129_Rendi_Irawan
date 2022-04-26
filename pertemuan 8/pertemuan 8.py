import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = '5210411129_db'
)

class PerpusItem:
    def __init__(self,judul,subjek,lokasi):
        self.judul  = judul
        self.subjek = subjek
        self.lokasi = lokasi

class Buku(PerpusItem):
    def __init__(self,judul,subjek,lokasi,penerbit,tahunTerbit,jmlHal):
        super().__init__(judul,subjek,lokasi)
        self.penerbit    = penerbit
        self.tahunTerbit = tahunTerbit
        self.jmlHal      = jmlHal

class Majalah(PerpusItem):
    def __init__(self,judul,subjek,lokasi,volume,edisi):
        super().__init__(judul,subjek,lokasi)
        self.volume = volume
        self.edisi  = edisi
        
class DVD(PerpusItem):
    def __init__(self,judul,subjek,lokasi,aktor,genre):
        super().__init__(judul,subjek,lokasi)
        self.aktor = aktor
        self.genre = genre

pilihan = int(input("1. Buku\n2. Majalah\n3. DVD\nPilih Opsi Yang anda inginkan : "))
cur = db.cursor()
idSubjek = input("Masukkan ID: ")
cur.execute("SELECT * FROM perpus where id ="+idSubjek)
hasil = cur.fetchall()
for indeks in hasil:
    if pilihan == 1:
        book = [Buku(indeks[1],'Novel Ringan',indeks[2],indeks[3],indeks[4],indeks[5])]
        for dft in book:
            print("\nJudul         : {}\nTipe          : {}\nLokasi        : {}\nPenerbit      : {}\nTahun Terbit  : {}\nJumlah Halaman: {}".format(dft.judul,dft.subjek,dft.lokasi,dft.penerbit,dft.tahunTerbit,dft.jmlHal))

    elif pilihan == 2:
        magazine = [Majalah(indeks[1],'Majalah Anak',indeks[2],indeks[6],indeks[7])]
        for dft in magazine:
            print("\nJudul         : {}\nTipe          : {}\nLokasi        : {}\nVolume        : {}\nEdisi         : {}".format(dft.judul,dft.subjek,dft.lokasi,dft.volume,dft.edisi))

    elif pilihan == 3:
        dvd = [DVD(indeks[1],"Kaset DVD",indeks[2],indeks[8],indeks[9])]
        for dft in dvd:
            print("\nJudul         : {}\nTipe          : {}\nLokasi        : {}\nAktor         : {}\nGenre         : {}".format(dft.judul,dft.subjek,dft.lokasi,dft.aktor,dft.genre))
