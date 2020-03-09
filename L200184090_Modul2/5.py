class Mahasiswa():
    def __init__(self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
        self.daftar = []
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
    def ambilKotaTinggal(self):
        return self.kotaTinggal
    def perbaruiKotaTinggal(self, kotaBaru):
        self.kotaTinggal = kotaBaru
    def tambahUangSaku(self, tambahUang):
        self.uangSaku += tambahUang
    def listKuliah(self):
        return self.daftar
    def ambilKuliah(self, mataKuliah):
        self.daftar.append(mataKuliah)
    def hapusKuliah(self, hapus):
        self.daftar.remove(hapus)
