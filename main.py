from cisla import cisla

def vymaz_obrazovku():
    print(f"""{chr(27)}[2J""", end="")

def skryt_kurzor():
    print(f"""{chr(27)}[?25l""", end="")

def odkryt_kurzor():
    print(f"""{chr(27)}[?25h""", end="")

def nastav_pozici(x, y):
    print(f"\x1b[{y};{x}H", end="")

vymaz_obrazovku()
nastav_pozici(10, 3)
input()