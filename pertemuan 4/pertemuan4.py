class Segitiga:
    def __init__(self,alas,tinggi):
        self.alas = alas
        self.tinggi = tinggi
        self.luas = 0.5 * alas * tinggi

segitiga_besar = Segitiga(100,80)

#akses variabel public : alas, tinggi, dan luas dari luar segitiga
print('alas : ',segitiga_besar.alas)
print('tinggi : ',segitiga_besar.tinggi)
print('luas : ',segitiga_besar.luas)



class Utama:
    def __init__(self):
        self._a = 2

class Turunan(Utama):
    def __init__(self):
        #memanggil konstruktor pada kelas utama
        Utama.__init__(self)
        print('memanggil variabel protected pada class Utama',self._a)

        #modify the protected variabel
        self._a = 3
        print('memanggil variabel protected yang dimodifikasi diluar class', self._a)

object1 = Turunan()
object2 = Utama()

#memanggil variabel protected
print('Mengakses variabel protected dari object1 : ',object1._a)
print('mengakses variabel protected dari object2 : ',object2._a)



class Hitung:
    def __init__(self): #Function dengan metode __init__ menyimpan satu parameter (self)
        self.__angkaRahasia = 0 #Atribut bersifat Private

    def tampilkanhitung(self): #Function tampilkan hitung dengan parameter (self)
        self.__angkaRahasia += 1 #Atribut bersifat Private
        print(self.__angkaRahasia)   #cetak atribut  

#panngil function Hitung
hitungan =Hitung()
hitungan.tampilkanhitung()
hitungan.tampilkanhitung()

print(hitungan._Hitung__angkaRahasia)


#semua variabel bersipat public
class Mobil ():
    def __init__(self,jendela,pintu,mesin):
        self.jendela = jendela
        self.pintu = pintu
        self.mesin = mesin

#semua variabel bersifat protected
class Mobil ():
    def __init__(self,jendela,pintu,mesin):
        self._jendela = jendela
        self._pintu = pintu
        self._mesin = mesin

class Truk(Mobil):
    def __init__(self,jendela,pintu,mesin,tipe):
        super().__init__(jendela,pintu,mesin)
        self.tipebak = tipe

#semua variabel bersifat private
class Mobil():
    def __init__(self,jendela,pintu,mesin):
        self.__jendela =jendela
        self.__pintu = pintu
        self.__mesin = mesin

#fungsi private dan public
class Pegawai:
    __nama=''
    __alamat=''
    __gaji=0

    def __init__(self,nama,alamat):
        self.__nama=nama
        self.__alamat=alamat

    def __hitungGaji(self):
        upahLembur=20000
        gajiPokok=2000000
        jumLembur=int(input('Total jam lembur : '))
        self.__gaji=(upahLembur*jumLembur)+gajiPokok
    
    def tampilDetail(self):
        print('\n--menghitung dan menampilkan gaji pegawai--')
        print('Nama : ',self.__nama)
        print('Alamat : ',self.__alamat)
        self.__hitungGaji()
        print('Total Gaji : ',self.__gaji)

#membuat objek pegawai
pgw1=Pegawai('mikasa Ackerman','wall rose')
pgw1.tampilDetail()

pgw2=Pegawai('saya kisaragi','prefektur nagano')
pgw2.tampilDetail()


