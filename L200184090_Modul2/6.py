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

class SiswaSMA(Manusia):
    def __init__(self, nama, absen, sekolah, us):
        self.nama = nama
        self.noAbsen = absen
        self.sekolah = sekolah
        self.uangSaku = us
    def __str__(self):
        s = self.nama+ ", No Absen " + str(self.noAbsen) \
            + ". sekolah di " + self.sekolah \
            + ". Uang saku Rp " + str(self.uangSaku) \
            + " tiap minggunya."
        return s
    def ambilNama(self):
        return self.nama
    def ambilNoAbsen(self):
        return self.noAbsen
    def ambilUangSaku(self):
        return self.uangSaku
    def ambilSekolah(self):
        return self.sekolah
