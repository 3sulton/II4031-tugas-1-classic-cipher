import random
import string
import datetime
from be_vigenere import vigenere


class otp(vigenere):
    def __init__(self, M, K, C):
        super().__init__(M, K, C)
    
    def generate_key(self):
        letters = string.ascii_uppercase
        length = random.randint(10000, 99999)
        self.K = "".join(random.choices(letters, k=length))

        self.key_filename = "key-" + datetime.datetime.now().strftime("%H%M%S-%Y%m%d") + ".txt"
        key_dir = "../key/"
        with open(key_dir + self.key_filename, "w") as key_file:
            key_file.write(self.K)

def test_generate_key():
    o = otp("", "", "")
    o.generate_key()

def test_otp_encrypt():
    o = otp("aaa", "", "")
    m_awal = o.M
    o.generate_key()
    o.encrypt()
    o.M = ""
    o.decrypt()
    assert o.M == m_awal

if __name__ == "__main__":
    test_otp_encrypt()
    print("Everything passed")