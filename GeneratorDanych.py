from random import randint
import operator
import re

def generator_danych ():
    print("1. Wygeneruj i zapisz dane")
    print("2. Wczytaj dane")
    wybor = int(input("Numer opcji: "))


    if wybor == 1:
        lista_odwolan = []
        wielkosc_listy_odwolan = int(input("Wielkosc listy odwolan: "))
        min_liczba_w_liscie = int(input("Minimalna liczba w liscie odwolan: "))
        max_liczba_w_liscie = int(input("Maksymalna liczba w liscie odwolan: "))

        for k in range(wielkosc_listy_odwolan):
            lista_odwolan.append(randint(min_liczba_w_liscie, max_liczba_w_liscie))

        f = open("dane", "w")
        f.write(str(lista_odwolan))
        f.close()

        return lista_odwolan

    elif wybor == 2:
        lista_odwolan = []
        nazwa_pliku = input("Podaj nazwe pliku: ")
        f_do_odczytu = open(nazwa_pliku, "r")
        f_do_zapisu = open("dane", "w")

        for linia in f_do_odczytu:
            f_do_zapisu.write(linia)
            for word in linia.split(","):
                a = re.sub("\[|\]", "", word)

                lista_odwolan.append(int(a))

        f_do_zapisu.close()
        f_do_odczytu.close()

        return lista_odwolan