from Project3_files.crypto_utils import modular_inverse
from affine import affine
from caesar import caesar
from multiplikasjons_cypher import multiplikasjons_cypher
from person import person
from ubrytelige import ubrytelige


class hacker(person):
    """Hacker class"""

    def __init__(self, cypher_alg):
        super().__init__(cypher_alg)
        self.count = []
        self.used_keys = []
        try:
            with open('english_words2.txt') as file:
                self.all_words = file.read().splitlines()
        except BaseException:
            print("There is no file")

    def hack(self, cypher):
        """Hoved hacker methode"""
        if isinstance(self.cypher_alg, caesar):
            for i in range(self.cypher_alg.mod_number):
                self.split_decoded(self.cypher_alg.decode(cypher, i), i)
        elif isinstance(self.cypher_alg, multiplikasjons_cypher):
            for i in range(self.cypher_alg.mod_number):
                self.split_decoded(
                    self.cypher_alg.decode(
                        cypher, modular_inverse(
                            i, self.cypher_alg.mod_number), i), i)
        elif isinstance(self.cypher_alg, affine):
            keys = [(i, j) for i in range(0, self.cypher_alg.mod_number)
                    for j in range(0, self.cypher_alg.mod_number)]
            for i in range(len(keys)):
                self.split_decoded(
                    self.cypher_alg.decode(
                        cypher,
                        (modular_inverse(
                            keys[i][0],
                            self.cypher_alg.mod_number),
                            keys[i][1])),
                    (keys[i][0],
                     keys[i][1]))
        elif isinstance(self.cypher_alg, ubrytelige):
            for word in self.all_words:
                self.split_decoded(self.cypher_alg.decode(cypher, word), word)
        return self.most_frequent()

    def split_decoded(self, decoded, key):
        for word in decoded.split():
            if word in self.all_words:
                self.used_keys.append(key)

    def most_frequent(self):
        counter = 0
        try:
            ele = self.used_keys[0]
            for i in self.used_keys:
                curr_frequency = self.used_keys.count(i)
                if (curr_frequency > counter):
                    counter = curr_frequency
                    print(ele)
                    ele = i
            return ele
        except BaseException:
            return False

    def operate_cypher(self, text):
        return self.cypher_alg.decode(text, self.key)
