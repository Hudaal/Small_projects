from person import person
#from sender import sender


class receiver(person):
    """receiver class"""
    def __init__(self, cypher_alg):
        super().__init__(cypher_alg)
        self.sender = ""
        self.encode_key = ""

    def set_sender(self, cypher_alg, sender, generate=False, encode_key=""):
        """which sender I am receiving from"""
        if generate:
            cypher_alg.generate_key()
        self.sender = sender
        self.encode_key = encode_key

    def operate_cypher(self, text):
        code = self.cypher_alg.decode(text, self.key, self.encode_key)
        return code
