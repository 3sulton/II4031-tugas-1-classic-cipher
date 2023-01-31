import numpy as np
from chiper import chiper

class playfair(chiper):
    def __init__(self, M, K, C):
        super().__init__(M, K, C)
        # matrix_key yang valuenya berupa integer
        # yang merepresentasikan huruf
        self.matrix_key = np.zeros((5, 5))

    def key_string_to_matrix(self):
        unique_letter = ""
        # masukkan letter unik dari key
        for c in self.C:
            if c != "J" and c not in unique_letter:
                unique_letter = unique_letter + c
        # masukkan sisa huruf yang tidak ada dalam unique key
        for i in range(26):
            letter = chiper.int_to_char(i)
            if letter != "J" and letter not in unique_letter:
                unique_letter = unique_letter + letter
        # masukkan unique key ke dalam matrix
        k = 0
        for i in range(5):
            for j in range(5):
                self.matrix_key[i][j] = chiper.char_to_int(unique_letter[k])
                k += 1
        
def test_key_string_to_matrix():
    pf = playfair("", "", "jalan ganesha sepuluh")
    pf.key_string_to_matrix()
    test = np.array([   ["A", "L", "N", "G", "E"],
                        ["S", "H", "P", "U", "B"],
                        ["C", "D", "F", "I", "K"],
                        ["M", "O", "Q", "R", "T"],
                        ["V", "W", "X", "Y", "Z"]   ])
    for i in range(5):
        for j in range(5):
            assert pf.matrix_key[i][j] == chiper.char_to_int(test[i][j])

if __name__ == "__main__":
    test_key_string_to_matrix()
    print("Everything passed")