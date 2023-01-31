import math

# p : plain char
# c : chiper char
# n : ukuran alfabet
# k : jumlah pergeseran
# M : himpunan plainteks
# K : himpunan kunci
# C : himpunan chiperteks

class chiper:
    def __init__(self, M, K, C) -> None:
        # removes all whitespace characters
        # TO DO : filter semua karakter selain alfabet
        self.M = "".join(M.split()).upper()
        self.K = "".join(K.split()).upper()
        self.C = "".join(C.split()).upper()

    def five_letter_format(self):
        formated = ""
        for i, c in enumerate(self.C):
            if i % 5 == 0 and i != 0 and i != len(self.C) - 1:
                formated = formated + " "
            formated = formated + c
        self.C = formated

    @staticmethod
    def e(p, k, n=26):
        return (p + k) % n
    
    def d(c, k, n=26):
        return (c - k) % n

    def char_to_int(c):
        return ord(c.upper()) - 65

    def int_to_char(n):
        return chr(n + 65)

# UNIT TEST
def test_char_to_int():
    assert chiper.char_to_int("a") == 0
    assert chiper.char_to_int("z") == 25

def test_int_to_char():
    assert chiper.int_to_char(chiper.char_to_int("a")) == "A"
    assert chiper.int_to_char(chiper.char_to_int("z")) == "Z"

def test_e():
    assert chiper.int_to_char(chiper.e(chiper.char_to_int("A"), chiper.char_to_int("B"))) == "B"
    assert chiper.int_to_char(chiper.e(chiper.char_to_int("Z"), chiper.char_to_int("Z"))) == "Y"

def test_d():
    assert chiper.int_to_char(chiper.d(chiper.char_to_int("B"), chiper.char_to_int("B"))) == "A"
    assert chiper.int_to_char(chiper.d(chiper.char_to_int("Y"), chiper.char_to_int("Z"))) == "Z"

def test_five_letter_format():
    chip = chiper("", "", "SUMIMASEN")
    chip.five_letter_format()
    assert chip.C == "SUMIM ASEN"

    chip.C = "INU"
    chip.five_letter_format()
    assert chip.C == "INU"

    chip.C = "ITADAKIMAS"
    chip.five_letter_format()
    assert chip.C == "ITADA KIMAS"

if __name__ == "__main__":
    test_char_to_int()
    test_int_to_char()
    test_e()
    test_d()
    test_five_letter_format()
    print("Everything passed")
