import random


class cypher:
    def __init__(self):
        self.alfa = "!\"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ" \
            "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ \t\n\r\x0b\x0c'"
        #self.alfa = string.printable
        # print(self.alfa)
        self.mod_number = len(self.alfa)
        self.key_encode = ""
        self.key_decode = ""

    def encode(self, klar_text, key):
        "encode"
        new_cypher = ""
        i = 0
        while i < len(klar_text):
            pos = i
            pos = (pos + key) % self.mod_number
            new_cypher += self.alfa[pos]
            i += 1
        return new_cypher

    def decode(self, cypher_befor, key):
        "decode"
        klar_text = ""
        i = 0
        while i < len(cypher_befor):
            pos = i
            pos = (pos % self.mod_number) - key
            klar_text += self.alfa[pos]
            i += 1
        return klar_text

    def verify(self, klar_text, result):
        i = 0
        for ele in klar_text:
            if ele != result[i]:
                print(ele)
                return False
            i += 1
        return True

    def generate_key(self, my_key=False):
        if my_key:
            self.key_encode = my_key
            self.key_decode = my_key
        else:
            self.key_encode = random.randint(0, 100)
            self.key_decode = self.key_encode
