class Pesan(object):
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumKar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print("Kalimatku mempunyai", len(self.teks), "karakter")
    def perbarui(self, stringBaru):
        self.teks = stringBaru
    def apakahTerkandung(self, cari):
        if cari in self.teks:
            return True
        else:
            return False
    def hitungKonsonan(self):
        y = 0
        x = ("A", "I", "U", "E", "O", "a", "i", "u", "e", "o")
        for i in self.teks:
            if i not in x:
                y += 1
            else:
                continue
        return y
    def hitungVokal(self):
        y = 0
        x = ("A", "I", "U", "E", "O", "a", "i", "u", "e", "o")
        for i in self.teks:
            if i in x:
                y += 1
            else:
                continue
        return y
