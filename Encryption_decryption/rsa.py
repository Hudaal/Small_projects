import random

from Project3_files.crypto_utils import generate_random_prime, modular_inverse, blocks_from_text, text_from_blocks
from cypher import cypher


class rsa(cypher):
    def __init__(self):
        super().__init__()

    def encode(self, klar_text, key):
        new_cypher = ""
        self.blocks = []
        try:
            self.blocks.append(int(klar_text))
        except:
            self.blocks = blocks_from_text(klar_text, int(self.ran_bit/4))
        new_list = []
        for block in self.blocks:
            new_list.append(pow(block, self.key_encode[1], self.key_encode[0]))
        new_cypher = text_from_blocks(new_list, int(self.ran_bit / 4))
        return new_cypher

    def decode(self, cypher_befor, key, encode_key=""):
        klar_text = text_from_blocks(self.blocks, int(self.ran_bit/4))
        return klar_text


    def generate_key(self, my_key=False):
        self.ran_bit = 6
        p = generate_random_prime(self.ran_bit)
        q = generate_random_prime(self.ran_bit)
        while p == q:
            q = generate_random_prime(self.ran_bit)
        n = p*q
        pi = (p-1)*(q-1)
        e = random.randint(3, pi-1)
        d = modular_inverse(e, pi)
        self.key_encode = (n, e)
        self.key_decode = (n, d)
        return (self.key_encode, self.key_decode)