#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymorphy2

#перерводим глагол в нужную форму в зависимости от времени

def verbchange(vvod):
    morph = pymorphy2.MorphAnalyzer()
    lst = vvod.split()
    listvi=[]
    for el in lst:
        p =  morph.parse(el)[0]
        if {'VERB'} in p.tag:
            if {'pres'} in p.tag:
                if {'3per'} not in p.tag:
                   el = p.inflect({'plur','2per'}).word
            if {'futr'} in p.tag:
                if {'3per'} not in p.tag:
                   el = p.inflect({'plur','2per'}).word
            if {'past'} in p.tag:
                el = p.inflect({'plur'}).word

        listvi.append(el)



    vivod = ' '.join(listvi)

    return vivod



