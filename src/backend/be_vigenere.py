from chiper import chiper

class vigenere(chiper):
    def __init__(self, M="", K="", C=""):
        super().__init__(M, K, C)
    
    def encrypt(self):
        # for every m will be encrypted using k sesuai urutannya
        self.C = ""
        for i, m in enumerate(self.M):
            i = i % len(self.K)
            self.C = self.C + chiper.int_to_char(chiper.e(chiper.char_to_int(m), chiper.char_to_int(self.K[i])))

    def decrypt(self):
        self.M = ""
        for i, c in enumerate(self.C):
            i = i % len(self.K)
            self.M = self.M + chiper.int_to_char(chiper.d(chiper.char_to_int(c), chiper.char_to_int(self.K[i])))

def test_vigenere_encrypt():
    vig = vigenere("abc", "aaa", "")
    vig.encrypt()
    assert vig.C == "ABC"

    vig = vigenere("ab c", "b", "")
    vig.encrypt()
    assert vig.C == "BCD"

    vig = vigenere("ab c ", "ab cd", "")
    vig.encrypt()
    assert vig.C == "ACE"

    vig = vigenere("thisplaintext", "sony", "")
    vig.encrypt()
    assert vig.C == "LVVQHZNGFHRVL"

    vig = vigenere("Dinas Pendidikan Kota Ternate meminta kepada pihak sekolah dan\
orang tua siswa untuk jenjang pendidikan SD dan SMP seKota Ternate\
untuk melarang para siswa membawa permainan latolato yang sedang\
tren itu ke sekolah karena akan mengganggu kegiatan belajar mengajar\
yang dinilai berbahaya sehingga mengantisipasi kecelakaan bagi anak di\
daerah itu", "selatsunda", "")
    vig.encrypt()
    assert vig.C == "VMYALHYAGIVMVAGCIGDTWVYAMWGRPIFXLKXHUQDPALLKLWEBOA\
ZHLNHJUAJTMEDILOUHQTMOUEGBUAJPWROIWAENQSVHLNLEJFHK\
GXLTXJHNWEMREUDEYYDRSRRPTJUFLSOEXEFTUJDPWVXABFUAOA\
LSWAMGSNQGKIOAGYNEHNAXFKXKYXRLSLVAKWHNDKSRXEGYANQG\
YYVEZAUGDNTIWACSLZHNYEUAKQUAJDARTLTAVRUBSLLYTKYULNYKLMX\
FANQTAWTPTKCXHCWPLKTSHODGAEYADVCQDEJESIMM"

def test_vigenere_decrypt():
    vig = vigenere("", "aaa", "abc")
    vig.decrypt()
    assert vig.M == "ABC"

    vig = vigenere("", "b", "bc d")
    vig.decrypt()
    assert vig.M == "ABC"

    vig = vigenere("", "ab cd", " a c e ")
    vig.decrypt()
    assert vig.M == "ABC"

    vig = vigenere("", "sony", "LVVQHZNGFHRVL")
    vig.decrypt()
    assert vig.M == "THISPLAINTEXT"

    vig = vigenere("", "selatsunda", "VMYALHYAGIVMVAGCIGDTWVYAMWGRPIFXLKXHUQDPALLKLWEBOA\
ZHLNHJUAJTMEDILOUHQTMOUEGBUAJPWROIWAENQSVHLNLEJFHK\
GXLTXJHNWEMREUDEYYDRSRRPTJUFLSOEXEFTUJDPWVXABFUAOA\
LSWAMGSNQGKIOAGYNEHNAXFKXKYXRLSLVAKWHNDKSRXEGYANQG\
YYVEZAUGDNTIWACSLZHNYEUAKQUAJDARTLTAVRUBSLLYTKYULNYKLMX\
FANQTAWTPTKCXHCWPLKTSHODGAEYADVCQDEJESIMM")
    vig.decrypt()
    assert vig.M == "DINASPENDIDIKANKOTATERNATEMEMINTAKEPADAPIHAKSEKOLAHDAN\
ORANGTUASISWAUNTUKJENJANGPENDIDIKANSDDANSMPSEKOTATERNATE\
UNTUKMELARANGPARASISWAMEMBAWAPERMAINANLATOLATOYANGSEDANG\
TRENITUKESEKOLAHKARENAAKANMENGGANGGUKEGIATANBELAJARMENGAJAR\
YANGDINILAIBERBAHAYASEHINGGAMENGANTISIPASIKECELAKAANBAGIANAKDI\
DAERAHITU"

if __name__ == "__main__":
    test_vigenere_encrypt()
    test_vigenere_decrypt()
    print("Everything passed")