import random

from Project3_files.crypto_utils import modular_inverse
from caesar import caesar
from cypher import cypher
from multiplikasjons_cypher import multiplikasjons_cypher


class ubrytelige(cypher):
    def __init__(self):
        super().__init__()
        self.caesar = caesar()

    def encode(self, klar_text, key):
        keys = self.get_keys_pos(klar_text, key)
        new_cypher = ""
        i = 0
        while i < len(klar_text):
            new_cypher += self.caesar.encode(klar_text[i], keys[i])
            i += 1
        #print("new_cypher: ", new_cypher)
        return new_cypher

    def decode(self, cypher_befor, key, encode_key=""):
        keys = self.get_keys_pos(cypher_befor, key)
        klar_text = ""
        # print(len(keys))
        #print("befor: "+cypher_befor)
        i = 0
        while i < len(cypher_befor):
            klar_text += self.caesar.decode(cypher_befor[i], keys[i])
            i += 1
        return klar_text

    def get_keys_pos(self, klar_text, key):
        count = 0
        i = 0
        keys = []
        while count < len(klar_text):
            keys.append(self.alfa.index(key[i]))
            i = (i + 1) % len(key)
            count += 1
        return keys

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
            self.key_decode = my_key
        else:
            length = random.randint(0, len(self.alfa) - 1)
            self.key_encode = ""
            self.key_decode = ""
            for i in range(length):
                self.key_encode += self.alfa[random.randint(
                    0, len(self.alfa) - 1)]
                self.key_decode += self.key_encode[i]
        return (self.key_encode, self.key_decode)
