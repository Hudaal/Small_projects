"""Tilfeldig klasse"""

import random


class Tilfeldig:
    """Tilfeldig klasse"""
    def __init__(self, spiller):
        self.spiller = spiller

    def tilfeldig(self):
        """Hoved metode"""
        return self.spiller.all_valg[random.randint(0, 2)]
