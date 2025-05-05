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

while True:
    input = input("Valitse kategoria: (A) Ruoka (B) Luonto (C) Satunnainen")

    if input.lower == "a" or input.lower == "ruoka":