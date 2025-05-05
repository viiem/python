"""
Hirsipuu-peli
Arpoo sanojen joukosta jonkun sanan ja pelaajan tulee arvata se sana
#if input.lower == "b" or input.lower == "luonto":""
#if input.lower == "c" or input.lower == "satunnainen":"
"""
sanalistaRuoka = '''kinuskipehmis perunakellari viinirypäle porkkanalaatikko'''
sanalistaLuonto = '''kuparimalmi pajunkissa lumpeenlehti vaippapaviaani'''
sanalistaSatunnainen = '''sinkkunainen elämänkumppani alkoholinkäyttö pyykinpesupäivä'''

import random
from collections import Counter

print("Pelataan Hirsipuuta!")

saannot = input("Haluatko lukea säännöt ennen pelaamista?")
if saannot.lower == "kyllä":
    print("Tässä säännöt: Saat kolme mahdollisuutta.")
    print()
    print("Nyt pelataan!")
if saannot.lower == "ei":
    print("Nyt pelataan!")
else:
    print("Vastaa kyllä tai ei.")

while True:
    input = input("Valitse kategoria: (A) Ruoka (B) Luonto (C) Satunnainen")

    if input.lower == "a" or input.lower == "ruoka":
        sanalistaRuoka = sanalistaRuoka.split(' ')
        sana = random.choice(sanalistaRuoka)

        print("Arvaa sana! Sana liittyy aiheeseen ruoka")

        for i in sana:
            print('_', end=' ')
        print()
        pelataan = True
        arvattu = ''
        elamat = 3
        oikein = 0
        jatketaanko = 0
        try:
            while (elamat != 0) and jatketaanko == 0:
                print()
                elamat