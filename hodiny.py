#!/usr/bin/env python3
"""
Hodiny - program ukazuje aktuální systémový čas po 1s, program ukončíte stisknutím CTRL-C
"""
# modul pro práci s časem
import time
from cisla import cisla

cisla = [[radek.replace("*", str(x)) for radek in cislo] for x, cislo in enumerate(cisla)]
znaky = dict(zip([str(i) for i in range(len(cisla))], cisla))
znaky[":"] = [" ", ":", ":", ":", ":"]
print(f"""{chr(27)}[32m""", end="")

def vymaz_obrazovku():
    print(f"""{chr(27)}[2J""", end="")

def nastav_pozici(x, y):
    print(f"\x1b[{y};{x}H", end="")

def vypis_znak(znak, x, y):
    znak = znaky[znak]
    for radek in znak:
        nastav_pozici(x, y)
        print(radek, end="")
        y += 1

def vypis_cas(cas):
    vymaz_obrazovku()
    mezera_mezi_cisly = 3
    mezera_u_dvojtecky = 4
    x = 2
    y = 2
    for znak in cas:
        x += mezera_u_dvojtecky if (znak == ":") else mezera_mezi_cisly
        vypis_znak(znak, x, y)
        x += mezera_u_dvojtecky if (znak == ":") else 0
        x += + len(znaky[znak][0])
#Skryti kurzoru
print(f"""{chr(27)}[?25l""", end="")
## hlavní programová smyčka
while True:
    # získání údaje o aktuálním čase ve formátu hodiny:minuty:sekundy
    # string, formated time
    display = time.strftime("%H:%M:%S")
    # vytištění získaného času
    vypis_cas(display)
    # program se na 1s zastaví
    time.sleep(1)
####### KONEC PROGRAMU #####