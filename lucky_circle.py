#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last modified: Wang Tai (i@wangtai.me)

class Result(object):
    def __init__(self, num):
        self.num = num

    def is_odd(self):
        if self.num == 0:
            return None
        return self.num%2 == 1

    def is_red(self):
        if self.num == 0:
            return None
        return self.num%2 == 1

    def get_num(self):
        return self.num

#print "num: {}, odd: {}, red: {}".format(r.get_num(), r.is_odd(), r.is_red())


class Select(object):
    coin = 0
    red = None

    def add_coin(self, coin):
        self.coin += coin
        return self

    def select_color(self, color):
        self.red = color == 'red'
        return self


class Rule(object):
    def __init__(self, result, select):
        self.res = result
        self.select = select

    def reward(self):
        try:
            if self.select.red is not None:
                if self.res.is_red() != self.select.red:
                    return 0 - self.select.coin

                return self.select.coin

            return 0
        finally:
            #print "You selected color: {}, the result is {}".format(self.select.red, self.res.is_red())
            pass

def play(init_wallet):
    max_coin = 2000
    my_wallet = init_wallet
    init_coin = 10
    coin = init_coin

    display_stack = []
    ds_s = 0
    ds_l = 11
    red_count = 0
    green_count = 0
    none_count = 0
    for i in range(10000):
        if coin > max_coin:
            coin = init_coin
            #pass

        if coin > my_wallet:
            #print "Coin {}, Wallet {}".format(coin, my_wallet)
            coin = my_wallet

        if my_wallet <= 0:
            print "You Lost! You play {} times".format(i+1)
            return False

        if red_count < green_count:
            color = 'red'
        elif red_count > green_count:
            color = 'green'
        else:
            color = None

        select = Select().add_coin(coin).select_color(color)
        import random
        lucky_ball = random.choice(range(37))

        r = Result(lucky_ball)

        display_stack.append(r.is_red())
        if r.is_red():
            red_count += 1
        elif r.is_red() is None:
            none_count += 1
        else:
            green_count += 1

        reward = Rule(r, select).reward()
        my_wallet += reward

        if reward > 0:
            coin = init_coin
        else:
            coin *= 2


    print "red {} green {} none {}".format(red_count, green_count, none_count)
    if my_wallet >= init_wallet:
        print "You Win! Your wallet: {}".format(my_wallet)
        #print "Max Coin {}".format(max_coin)
        return True
    else:
        print "You Lost! Your wallet: {}".format(my_wallet)
        #print "Max Coin {}".format(max_coin)
        return False


lost_count = 0
win_count = 0
for i in range(100):
    if play(10000):
        win_count += 1
    else:
        lost_count += 1

print "Win Count: {}, Lost Count: {}".format(win_count, lost_count)
