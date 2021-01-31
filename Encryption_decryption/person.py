class person:
    """Basic persone class"""
    def __init__(self, cypher_alg):
        self.cypher_alg = cypher_alg
        self.key = 0

    def set_key(self, key):
        """put the key"""
        self.key = key

    def get_key(self):
        """get the key"""
        return self.key

    def operate_cypher(self, text):
        """Will be overrided"""
        return self.cypher_alg.encode(text, self.key)
