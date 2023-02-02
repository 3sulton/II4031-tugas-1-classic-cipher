import numpy as np
from chiper import chiper

class playfair(chiper):
    def __init__(self, M, K, C):
        super().__init__(M, K, C)
        # matrix_key yang valuenya berupa huruf
        self.matrix_key = np.full((5, 5), "A")
        self.key_string_to_matrix()

    def key_string_to_matrix(self):
        unique_letter = ""
        # masukkan letter unik dari key
        for k in self.K:
            if k != "J" and k not in unique_letter:
                unique_letter = unique_letter + k
        # masukkan sisa huruf yang tidak ada dalam unique key
        for i in range(26):
            letter = chiper.int_to_char(i)
            if letter != "J" and letter not in unique_letter:
                unique_letter = unique_letter + letter
        # masukkan unique key ke dalam matrix
        k = 0
        for i in range(5):
            for j in range(5):
                self.matrix_key[i][j] = unique_letter[k]
                k += 1

    def encrypt(self):
        i = 0
        msg_length = len(self.M)
        while (i < msg_length):
            # SETUP 2 KARAKTER AWAL DULU
            # karakter pertama
            m1 = self.M[i]
            # karakter kedua
            # jika i adalah terakhir maka ganti dengan x
            if i == msg_length - 1:
                m2 = "X"
            else:
                m2 = self.M[i + 1]
            # ganti huruf j dengan i
            if m1 == "J":
                m1 = "I"
            if m2 == "J":
                m2 = "I"
            # ganti m2 dengan x apabila m1 == m2
            if m1 == m2:
                m2 = "X"
                i += 1
            else:
                assert m1 != m2
                i += 2
            
            # ALGORITMA UNTUK ENKRIP DENGAN MELIHAT KEY MATRIKS
            # Periksa index dari tiap message
            idx_m1 = np.where(self.matrix_key == m1)
            idx_m2 = np.where(self.matrix_key == m2)
            (r1, c1) = idx_m1[0][0], idx_m1[1][0]
            (r2, c2) = idx_m2[0][0], idx_m2[1][0]
            # jika dalam baris yang sama
            if r1 == r2:
                self.C = self.C + \
                self.matrix_key[r1][(c1 + 1) % 5] + self.matrix_key[r2][(c2 + 1) % 5]
            elif c1 == c2:
                self.C = self.C + \
                self.matrix_key[(r1 + 1) % 5][c1] + self.matrix_key[(r2 + 1) % 5][c2]
            else:
                self.C = self.C + \
                self.matrix_key[r1][c2] + self.matrix_key[r2][c1]


        
def test_key_string_to_matrix():
    pf = playfair("", "jalan ganesha sepuluh", "")
    test = np.array([   ["A", "L", "N", "G", "E"],
                        ["S", "H", "P", "U", "B"],
                        ["C", "D", "F", "I", "K"],
                        ["M", "O", "Q", "R", "T"],
                        ["V", "W", "X", "Y", "Z"]   ])
    for i in range(5):
        for j in range(5):
            assert pf.matrix_key[i][j] == test[i][j]

def test_encrypt():
    pf = playfair("di", "jalan ganesha sepuluh", "")
    pf.encrypt()
    assert pf.C == "FK"

    pf = playfair("qt", "jalan ganesha sepuluh", "")
    pf.encrypt()
    assert pf.C == "RM"

    pf = playfair("nq", "jalan ganesha sepuluh", "")
    pf.encrypt()
    assert pf.C == "PX"

    pf = playfair("ow", "jalan ganesha sepuluh", "")
    pf.encrypt()
    assert pf.C == "WL"\
    
    pf = playfair("hz", "jalan ganesha sepuluh", "")
    pf.encrypt()
    assert pf.C == "BW"

    pf = playfair("zh", "jalan ganesha sepuluh", "")
    pf.encrypt()
    assert pf.C == "WB"

    pf = playfair("temui ibu nanti malam", "jalan ganesha sepuluh", "")
    pf.encrypt()
    assert pf.C == "ZBRSFYKUPGLGRKVSNLQV"


if __name__ == "__main__":
    test_key_string_to_matrix()
    test_encrypt()
    print("Everything passed")