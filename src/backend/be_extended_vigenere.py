from chiper import chiper
from be_vigenere import vigenere

class extendedVigenere(vigenere):
    def __init__(self, M="", K="", C=""):
        super().__init__(M, K, C)

    def read_bytecode(self, filename):
        self.filename = filename
        with open(filename, "rb") as file:
            return bytearray(file.read())

    def ascii_to_int(self, c):
        return ord(c)

    def int_to_ascii(self, n):
        return chr(n)

    def encrypt(self, filename, fileout):
        self.byte_encrypt(filename, fileout)
    
    def decrypt(self, filename, fileout):
        self.byte_decrypt(filename, fileout)

    def byte_encrypt(self, filename, fileout):
        self.C = self.read_bytecode(filename)
        i = 0
        j = 0
        while (i < len(self.C)):
            self.C[i] = chiper.e(self.C[i], chiper.char_to_int(self.K[j]), 256)
            i += 1
            j = (j + 1) % len(self.K)

        with open(fileout, "wb") as file:
            file.write(bytes(self.C))
    
    def byte_decrypt(self, filename, fileout):
        self.M = self.read_bytecode(filename)
        i = 0
        j = 0
        while (i < len(self.M)):
            self.M[i] = chiper.d(self.M[i], chiper.char_to_int(self.K[j]), 256)
            i += 1
            j = (j + 1) % len(self.K)

        with open(fileout, "wb") as file:
            file.write(bytes(self.M))

def test_encrypt():
    ev = extendedVigenere(K="b")
    ev.encrypt("../file/1.jpg", "../file/1-e.jpg")

def test_decrypt():
    ev = extendedVigenere(K="b")
    ev.decrypt("../file/1-e.jpg", "../file/1-d.jpg")

if __name__ == "__main__":
    test_encrypt()
    test_decrypt()
    print("Everything passed")