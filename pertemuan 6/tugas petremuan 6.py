# #Overloading Class ComputerPart

# class ComputerPart(): #Class computer
#     def __init__ (self,jenis):
#         self.jenis = jenis #Atribut public
    
#     #function processeor menyimpan parameter nama, harga , pabrikan
#     def Processor(self, nama = None, harga = None, pabrikan = None): 
#         computerpart_3.display_Computer() #Panggil function display_computer
#         print("Nama Processor      : ",nama)
#         print("Harga               : ",harga)
#         print("Pabrikan            : ",pabrikan,"\n") #\n untuk menambakan enter satu pada saat di run
    
#     #function processeor menyimpan parameter nama, harga , pabrikan
#     def RandomAccessMemory(self, nama = None, harga = None, pabrikan = None):
#         computerpart_1.display_Computer()
#         print("Nama RAM            : ",nama)
#         print("Harga               : ",harga)
#         print("Pabrikan            : ",pabrikan,"\n")

#     #function processeor menyimpan parameter nama, harga , pabrikan
#     def HardiskSATA(self, nama = None, harga = None, pabrikan = None):
#         computerpart_2.display_Computer()
#         print("Nama Hardisk        : ",nama)
#         print("Harga               : ",harga)
#         print("Pabrikan            : ",pabrikan,"\n")
    
#     def display_Computer(self): 
#         print("Jenis computer part : ",self.jenis)

# #Membuat objek
# computerpart_1 = ComputerPart("Processor")
# computerpart_2 = ComputerPart ("RAM")
# computerpart_3 = ComputerPart ("Hardisk")

# #Menambahakan Overloading
# computerpart_1.Processor("AMD Ryzen 5",1350000,"AMD")
# computerpart_2.RandomAccessMemory("KINGSTON HYPERX FURY",365000,"Kingston")
# computerpart_3.HardiskSATA("Hardisk WDC Blue",410000,"WD Blue")











#Overriding Class ComputerPart

class ComputerPart(): #Class computer atau class induk
    def __init__ (self,pabrikan,harga):
        self.pabrikan = pabrikan #Atribut public
        self.harga = harga 
    
    def display(self): #Function untuk menampilkan data
        print("Pabrikan : ",self.pabrikan) 
        print("Harga    : ", self.harga,"\n") #\n untuk memnambakan enter satu kali ketika di run

class Processor(ComputerPart): 
    def __init__(self,nama,jumlah_core,speed):
        self.nama = nama 
        self.jumlah_core = jumlah_core 
        self.speed = speed 

    def display(self): # Function display untuk menampilkan data
        print("Nama Processor : ",self.nama)
        print("jumlah core    : ",self.jumlah_core)
        print("Speed          : ", self.speed)

#Membuat objek
processor_1 = ComputerPart("Intel", 6000000)
processor_1.display()

# Methode Overriding
# Mengabaikan metode yang dari induk dan mendefinisikan sendiri metode dengan nama yang sama di kelas anak.
# Dan yang dijalankan adalah metode yang ada di kelas anak.
processor_2 = Processor("Intel Core i7",6,"2.4 Ghz")
processor_2.display()