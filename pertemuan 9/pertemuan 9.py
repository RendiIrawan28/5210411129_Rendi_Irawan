class gaji :
    def __init__(self, gaji_bulanan):
        self.gaji_bulanan = gaji_bulanan

    def total(self):
        return (self.gaji_bulanan*12)


class Pegawai :
    jumlah = 0
    def __init__(self, gaji_bulanan, bonus, nama):
        self.gaji_bulanan=gaji_bulanan
        self.bonus= bonus
        self.obj_gaji = gaji(self.gaji_bulanan)
        self.nama = nama
        Pegawai.jumlah += 1

    def hasil_tahunan(self):
        return "Total : "+ str(self.obj_gaji.total() + self.bonus)+ " rupiah"      

    def tampiljumlah():
        print('Total Gaji Pegawai : ', Pegawai.jumlah)
    
    def tampilpegawai(self):
        print("Nama :",self.nama, "Gaji : ", self.gaji_bulanan, "Bonus  : ", self.bonus)

    def tunjangan(self, istri=None, anak=None):
        if anak !=None and istri !=None:
            total = anak+istri
            print("Tunjangan Anak Dan Istri : ", total)
        else :
            total = istri
            print("Tunjangan Istri : ", total)

nama = str(input("Masukan Nama Pegawai    : "))
Gaji = int(input("Masukan Gaji  : "))
bonus = int(input("Masukan Bonus  : "))
istri = int(input("Masukan Tunjangan Istri   : "))
anak = int(input("Masukan Tunjangan Anak : "))

pegawai1 = Pegawai(Gaji, bonus,nama)
pegawai2 = Pegawai(Gaji, bonus, nama)
pegawai1.tampilpegawai()
pegawai2.tampilpegawai()
pegawai1.tunjangan(anak, istri)
pegawai2.tunjangan(istri)




print("Total pegawai  =  %d" % Pegawai.jumlah)
rataGaji = (pegawai1.gaji_bulanan + pegawai2.gaji_bulanan)/Pegawai.jumlah
print("Rata-rata gaji = "+ str(rataGaji))


print(pegawai1.hasil_tahunan())
print(pegawai2.hasil_tahunan())