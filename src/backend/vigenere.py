from chiper import chiper

class vigenere(chiper):
    def __init__(self, M, K, C):
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

if __name__ == "__main__":
    test_vigenere_encrypt()
    test_vigenere_decrypt()
    print("Everything passed")