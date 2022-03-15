#Hierachical Inheritance ComputerPart

class ComputerPart(): 
    def __init__ (self,pabrikan,nama,jenis,harga):
        self.pabrikan = pabrikan 
        self.nama = nama 
        self.jenis = jenis 
        self.harga = harga 
#Class porcessor dengan menyimpan parameter class ComputerPart
class Processor(ComputerPart):
    def __init__(self,pabrikan,nama,harga,jumlah_core,speed):
        super().__init__(pabrikan,nama,"processor",harga)
        self.jumlah_core = jumlah_core 
        self.speed = speed 

#Class RandomAccessMemory dengan menyimpan parameter class ComputerPart
class RandomAccessMemory(ComputerPart):
    def __init__(self,pabrikan,nama,harga,kapasitas):
        super().__init__(pabrikan,nama,"RAM",harga)
        self.kapasitas = kapasitas 

#Class HardDiskSATA dengan menyimpan parameter class ComputerPart
class HardDiskSATA(ComputerPart):
    def __init__(self,pabrikan,nama,harga,kapasitas,rpm):
        super().__init__(pabrikan,nama,"SATA",harga)
        self.kapasitas = kapasitas 
        self.rpm = rpm 

print("*****SPESIFIKASI COMPUTER*****","\n")
def display_processor():
    p =Processor("AMD","AMD Ryzen 5 2600",2050000,6,"3.4 GHz")
    print ("""Processor {} jumlah core {} harga {} kecepatan {} produksi dari {}"""
        .format(p.nama,p.jumlah_core,p.harga,p.speed,p.pabrikan)) 
display_processor() #panggil fungction untuk menampilkan data

def display_ram():
    r =RandomAccessMemory("Kingston FURY IMPACT ",8,795000,"Kingston")
    print ("""Ram {} dengan kapasitas {} GB harga Rp.{} produk dari {}"""
        .format(r.nama,r.kapasitas,r.harga,r.pabrikan)) 
display_ram() #panggil fungction untuk menampilkan data

def display_HDD():
    h =HardDiskSATA("HDD Seagate Barracuda",500,7200,199000,"Seagate Indonesia")
    print ("""Ram {} dengan kapasitas {} GB rpm {}  harga Rp.{} produk dari {}"""
        .format(h.nama,h.kapasitas,h.harga,h.rpm,h.pabrikan)) 
display_HDD() #panggil fungction untuk menampilkan data










print("*"*40)


#Multilevel Inheritance

class ComputerPart: 
    def __init__(self,pabrikan,nama,harga): 
        self.pabrikan =pabrikan 
        self.nama = nama
        self.harga = harga 

class Processor(ComputerPart): 
    def __init__(self,pabrikan,nama,harga):
        super().__init__(pabrikan,nama,harga) 
        

class RandomAccessMemory(Processor): 
    def __init__(self,pabrikan,nama,harga,kapasitas):
        super().__init__(pabrikan,nama,harga) 
        self.kapasitas = kapasitas 

r =RandomAccessMemory("Corsair","Corsair Venggegance",1242000,"16 GB")
print("Ram",r.nama,"harga",r.harga,"Kapasitas",r.kapasitas,"pabrikan dari",r.pabrikan)





print("*"*40)





#Multiple Inheritance ComputerPart

class HardDiskSATA_1(): 
    def __init__ (self,nama,pabrikan):
        self.nama = nama 
        self.pabrikan = pabrikan 
    
class HardDiskSATA_2():
    def __init__(self,kapasitas,harga):
        self.kapasitas = kapasitas
        self.harga = harga

class ComputerPart(HardDiskSATA_1,HardDiskSATA_2):
    def __init__(self,nama,pabrikan,kapasitas,harga):
        HardDiskSATA_1.__init__(self,nama,pabrikan)
        HardDiskSATA_2.__init__(self,kapasitas,harga)
        #cetak data
        print()
        print("""SSD {} kapasitas {} harga {} pabrikan dari {}"""
        .format(self.nama, self.kapasitas, self.harga, self. pabrikan))
        
#Membuat objek
ssd = ComputerPart("WD Green SATA","Western Digital","120 GB","Rp.1012000")