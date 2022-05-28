"""Warsztat: Symulator LOTTO.

Jak zapewne wiesz, LOTTO to gra liczbowa polegająca na losowaniu 6 liczb z zakresu 1 – 49.
Zadaniem gracza jest poprawne wytypowanie losowanych liczb.
Nagradzane jest trafienie 3, 4, 5 lub 6 poprawnych liczb.

Napisz program, który:

- zapyta o typowane liczby, przy okazji sprawdzi następujące warunki:
- czy wprowadzony ciąg znaków jest poprawną liczbą,
- czy użytkownik nie wpisał tej liczby już poprzednio,
- czy liczba należy do zakresu 1-49,
- po wprowadzeniu 6 liczb, posortuje je rosnąco i wyświetli na ekranie,
- wylosuje 6 liczb z zakresu i wyświetli je na ekranie,
- poinformuje gracza, ile liczb trafił.
"""
from random import randint

liczby = []
liczby_losowanie = []


def podaj_typowane_liczby():
    for i in range(6):
        while True:
            try:
                wprowadzona_liczba = int(input(f"Podaj liczbę nr {i + 1} >>>"))
                if 1 <= wprowadzona_liczba <= 60:
                    liczby.append(wprowadzona_liczba)
                    break
                else:
                    print("podano błędną liczbę")
            except ValueError:
                print("Value error")
    f"Wylosowano liczby {liczby}"
    return sorted(liczby)


def losowanie_lotto():
    for j in range(6):
        liczby_losowanie.append(randint(1, 60))
    return sorted(liczby_losowanie)


def sprawdzenie_wyniku(liczby, liczby_losowanie):
    if liczby == liczby_losowanie:
        print("Wygrałeś")
    else:
        print("Niestety nie trafiłeś")

    trafione = set(liczby) & set(liczby_losowanie)
    return print(f"Trafiłeś {len(trafione)} liczby: {str(trafione)}")



print("""
######################################
######SYMULATOR LOTTO#################
#################################byIT#
""")
print(podaj_typowane_liczby())
print(losowanie_lotto())
print(sprawdzenie_wyniku(liczby, liczby_losowanie))