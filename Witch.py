from HackFSU import Ability


class Witch (object):
    name = ''
    hp = 0
    ap = 0
    ability1 = MagicArrow
    ability2 = None

    def __init__(self, name, hp, ap, a1, a2):
        self.name = name
        self.hp = hp
        self.ap = ap
        self.ability1 = a1
        self.ability2 = a2


class YoungWitch(Witch):
    def __init__ (self, name, hp, ap, a1, a2):
        Witch (self, "Young Witch", 10, 4, MagicArrow, MeleeAttack)


class OldWitch (Witch):
    def __init__ (self, name, hp, ap, a1, a2):
        Witch (self, "Old Witch", 8, 3, MagicArrow, Fireball)
