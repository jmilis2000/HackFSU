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

class Fireball (Ability):
    def __init__ (self, name, rang, cell, ap, dmg):
        Ability(self, 'Fireball', 5, 4, 3, 1)

class MagicArrow (Ability):
    def __init__ (self, name, rang, cell, ap, dmg):
        Ability (self, 'Magic Arrow', 3, 1, 2, 2)

class MeleeAttack(Ability):
    def __init__ (self, name, rang, cell, ap, dmg):
        Ability (self, 'Magic Slap', 1, 1, 1, 1) 

