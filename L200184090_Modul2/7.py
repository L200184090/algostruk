class Manusia(object):
    keadaan = "lapar"
    def __init__(self, nama):
        self.nama = nama
    def ucapkanSalam(self):
        print("Salam, namaku", self.nama)
    def makan(self, s):
        print("Saya baru saja makan", s)
        self.keadaan = "kenyang"
    def olahraga(self, k):
        print("Saya baru saja latihan", k)
        self.keadaan = "lapar"
    def mengalikanDenganDua(self, n):
        return n*2

class Mahasiswa(Manusia):
    def __init__(self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama+ ", NIM " + str(self.NIM) \
            + ". Tinggal di " + self.kotaTinggal \
            + ". Uangsaku Rp " + str(self.uangSaku) \
            + " tiap bulannya."
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self, s):
        print("Saya baru saja makan", s, "sambil belajar.")
        self.keadaan = "kenyang"

class MhsTIF(Mahasiswa):
    def katakanPy(self):
        print("Python is cool")

a = MhsTIF("Ganno", 4092, "Solo", 200000)
a.ucapkanSalam() # from class Manusia
a.makan("Mie") # from class Mahasiswa
a.olahraga("renang") # from class Manusia
a.mengalikanDenganDua(18) # from class Manusia
a.ambilNama() # from class Mahasiswa
a.ambilNIM() # from class Mahasiswa
a.ambilUangSaku() # from class Mahasiswa
a.katakanPy() # from class MhsTIF
a.nama # from class Mahasiswa
a.NIM # from class Mahasiswa
a.kotaTinggal # from class Mahasiswa
a.uangSaku # from class Mahasiswa
