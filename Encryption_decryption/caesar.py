import random
from cypher import cypher

class caesar(cypher):
    """Key by addition"""
    def __init__(self):
        super().__init__()

    def encode(self, klar_text, key):
        """encode"""
        new_cypher = ""
        for ele in klar_text:
            pos = self.alfa.index(ele)
            pos = (pos + key) % self.mod_number
            new_cypher += self.alfa[pos]
        return new_cypher

    def decode(self, cypher_befor, key, encode_key=""):
        """decode"""
        klar_text = ""
        for ele in cypher_befor:
            pos = self.alfa.index(ele)
            pos = (pos % self.mod_number) - key
            klar_text += self.alfa[pos]
        return klar_text

    def generate_key(self, my_key=False):
        if my_key:
            self.key_encode = my_key
            self.key_decode = my_key
        else:
            self.key_encode = random.randint(0, self.mod_number)
            self.key_decode = self.key_encode
        return (self.key_encode, self.key_decode)
