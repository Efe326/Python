import random

class Dice:
    def roll(self, sides):
        return random.randint(1, sides)


class Enemy:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense

class Guard:
    def __init__(self, name, hp, attack, defense, art_defense, dmgtype, level=1, exp=0):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.art_defense = art_defense
        self.dmgtpye = dmgtype
        self.level = level
        self.exp = exp

    def gain_exp(self, amount):
        self.exp += amount
        if self.exp >= 100:
            self.level += 1
            self.exp = 0
            self.attack += 15
            self.defense += 30
            self.art_defense += 2


class Sniper:
    def __init__(self, name, hp, attack, defense, art_defense, dmgtype, level=1, exp=0):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.art_defense = art_defense
        self.dmgtpye = dmgtype
        self.level = level
        self.exp = exp

    def gain_exp(self, amount):
        self.exp += amount
        if self.exp >= 100:
            self.level += 1
            self.exp = 0
            self.attack += 15
            self.defense += 30
            self.art_defense += 2


class Caster:
    def __init__(self, name, hp, attack, defense, art_defense, dmgtype, level=1, exp=0):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.art_defense = art_defense
        self.dmgtpye = dmgtype
        self.level = level
        self.exp = exp

    def gain_exp(self, amount):
        self.exp += amount
        if self.exp >= 100:
            self.level += 1
            self.exp = 0
            self.attack += 15
            self.defense += 30
            self.art_defense += 2

class Defender:
    def __init__(self, name, hp, attack, defense, art_defense, dmgtype, level=1, exp=0):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.art_defense = art_defense
        self.dmgtpye = dmgtype
        self.level = level
        self.exp = exp

    def gain_exp(self, amount):
        self.exp += amount
        if self.exp >= 100:
            self.level += 1
            self.exp = 0
            self.attack += 15
            self.defense += 30
            self.art_defense += 2












