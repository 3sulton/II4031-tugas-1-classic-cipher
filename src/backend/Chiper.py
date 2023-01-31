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
        self.M = "".join(M.split())
        self.K = "".join(K.split())
        self.C = "".join(C.split())

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

if __name__ == "__main__":
    test_char_to_int()
    test_int_to_char()
    test_e()
    test_d()
    print("Everything passed")
