import random

from Project3_files.crypto_utils import modular_inverse
from caesar import caesar
from cypher import cypher
from multiplikasjons_cypher import multiplikasjons_cypher


class affine(cypher):
    def __init__(self):
        super().__init__()
        self.caesar = caesar()
        self.mul = multiplikasjons_cypher()

    def encode(self, klar_text, key):
        new_cypher = self.mul.encode(klar_text, key[0])
        new_cypher2 = self.caesar.encode(new_cypher, key[1])
        return new_cypher2

    def decode(self, cypher_befor, key, encode_key=""):
        klar_text = self.caesar.decode(cypher_befor, key[1])
        klat_text2 = self.mul.decode(klar_text, key[0], self.key_encode[0])
        return klat_text2

    def verify(self, klar_text, result):
        i = 0
        for ele in klar_text:
            if ele != result[i]:
                print("This key is not acceptable!")
                return False
            i += 1
        return True

    def generate_key(self, my_key=False):
        """my_key er tuble av lengde 2"""
        if my_key:
            self.key_encode = my_key
        else:
            self.key_encode = (
                random.randint(
                    0, self.mod_number), random.randint(
                    0, self.mod_number))
        self.key_decode = (
            modular_inverse(
                self.key_encode[0],
                self.mod_number),
            self.key_encode[1])
        return (self.key_encode, self.key_decode)
