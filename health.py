#! /usr/bin/env python
# Python 2.7
# created by Steve Bateman
# Copyright 2016, Creative Commons

import player
import random


#These are all the health potion available


class PotionWeak(object):
    name = "WEAK POTION"
    effect = 10 + player.user.level * 5
    weight = 2
    value = 20

    #Establishes the strength of the potion based on player's stats
    def enter(self):
        self.effect = 10 + player.user.level * 5


class PotionStrong(object):
    name = "STRONG POTION"
    effect = 20 + player.user.level * 10
    weight = 4
    value = 40

    #Establishes the strength of the potion based on player's stats
    def enter(self):
        self.effect = 20 + player.user.level * 10


class Elixer50(object):
    name = "ELIXER 50%"
    effect = (player.user.maxHp / 2)
    weight = 1
    value = 50

    #Establishes the strength of the elixer based on player's stats
    def enter(self):
        self.effect = (player.user.maxHp / 2)


class Elixer100(object):
    name = "ELIXER 100%"
    effect = (player.user.maxHp)
    weight = 2
    value = 80

    #Establishes the strength of the elixer based on player's stats
    def enter(self):
        self.effect = (player.user.maxHp)


#Called by map.py to load random potions/elixers
class HealthChooser(object):
    healthTypes = [
        PotionWeak(),
        PotionStrong(),
        Elixer50(),
        Elixer100()
    ]

    def enter(self):
        health = self.healthTypes[random.randint(0, 3)]
        return health

#health = HealthChooser().enter()
