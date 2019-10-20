class Ability:

    # Class variables
    name = ''
    range = 0
    cell = 0
    ap = 0
    dmg = 0

    def __init__(self, name, rang, cell, ap, dam):
        self.name = name
        self.range = rang
        self.cell = cell
        self.ap = ap
        self.dmg = dam

    def Fireball(self):
        self.name = 'Fireball'
        self.range = 5
        self.cell = 4
        self.ap = 3
        self.dmg = 1

    def MagicArrow(self):
        self.name = 'Magic Arrow'
        self.range = 3
        self.cell = 1
        self.ap = 2
        self.dmg = 2

    def MeleeAttack(self):
        self.name = 'Magic Slap'
        self.range = 1
        self.cell = 1
        self.ap = 1
        self.dmg = 1
