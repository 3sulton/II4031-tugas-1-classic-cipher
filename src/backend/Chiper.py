# p : plain text
# c : chiper text
# n : ukuran alfabet
# k : jumlah pergeseran
# M : himpunan plainteks
# K : himpunan kunci
# C : himpunan chiperteks

class chiper:
    def __init__(self, M, K, C) -> None:
        self.M = M
        self.K = K
        self.C = C

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

if __name__ == "__main__":
    test_char_to_int()
    print("Everything passed")
