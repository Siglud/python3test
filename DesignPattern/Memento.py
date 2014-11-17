# coding=utf-8
__author__ = 'Siglud'
#备忘录模式


class Character(object):
    health = 0
    attack = 0
    defence = 0

    def DisplayState(self):
        print("生命: %s" % self.health)
        print("攻击力: %s" % self.attack)
        print("防御力: %s" % self.defence)

    def initState(self):
        self.health = 100
        self.attack = 100
        self.defence = 100

    def Fight(self):
        self.health = 0
        self.attack = 0
        self.defence = 0

    def saveState(self):
        return RoleStateMemento(self.health, self.attack, self.defence)

    def recoveryState(self, memento):
        self.health = memento.health
        self.attack = memento.attack
        self.defence = memento.defence


class RoleStateMemento(object):
    health = 0
    attack = 0
    defence = 0

    def __init__(self, health, attack, defence):
        self.health = health
        self.attack = attack
        self.defence = defence


class RoleStateCreateTaker(object):
    memento = None
