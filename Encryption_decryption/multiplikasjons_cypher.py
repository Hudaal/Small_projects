import random
from Project3_files.crypto_utils import modular_inverse
from cypher import cypher


class multiplikasjons_cypher(cypher):
    """different key between sender and receiver"""
    def __init__(self):
        super().__init__()

    def encode(self, klar_text, key):
        """encode"""
        new_cypher = ""
        for ele in klar_text:
            pos = self.alfa.index(ele)
            pos = (pos * key) % self.mod_number
            new_cypher += self.alfa[pos]
        return new_cypher

    def decode(self, cypher_befor, key, encode_key=""):
        """decode"""
        klar_text = ""
        for ele in cypher_befor:
            pos = self.alfa.index(ele)
            pos = (pos * key % self.mod_number)
            klar_text += self.alfa[pos]
        return klar_text

    def verify(self, klar_text, result):
        i = 0
        for ele in klar_text:
            if ele != result[i]:
                print("This key is not acceptable!")
                return False
            i += 1
        return True

    def generate_key(self, my_key):
        if my_key:
            self.key_encode = my_key
        else:
            self.key_encode = random.randint(0, self.mod_number)
        self.key_decode = modular_inverse(self.key_encode, self.mod_number)
        return (self.key_encode, self.key_decode)