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

numbers = []
random_numbers = []


def typing_numbers():
    for i in range(6):
        while True:
            try:
                input_numbers = int(input(f"Podaj liczbę nr {i + 1} >>>"))
                if 1 <= input_numbers <= 60 and input_numbers not in numbers:
                    numbers.append(input_numbers)
                    break
                else:
                    print("podano błędną liczbę")
            except ValueError:
                print("Value error")
    f"Wylosowano liczby {numbers}"
    return sorted(numbers)


def lotto_draw():
    for j in range(6):
        random_numbers.append(randint(1, 60))
    return sorted(random_numbers)


def result_check(numbers, random_numbers):
    if numbers == random_numbers:
        print("Wygrałeś")
    else:
        print("Niestety nie trafiłeś")

    hit_numbers = set(numbers) & set(random_numbers)
    return print(f"Trafiłeś {len(hit_numbers)} liczby: {str(hit_numbers)}")



print("""
######################################
######SYMULATOR LOTTO#################
#################################byIT#
""")
print(typing_numbers())
print(lotto_draw())
print(result_check(numbers, random_numbers))