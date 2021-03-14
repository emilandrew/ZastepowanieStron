from GeneratorDanych import *

lista_odwolan = generator_danych()

slownik_wartosci = {}

for wartosc in lista_odwolan:
    slownik_wartosci[wartosc] = 0

max_ramek = int(input("Maksymalna ilosc ramek: "))
ramki_fifo = [None] * max_ramek
ramki = []

lista_wartosci = []

def get_key(wartosc):
    for key, value in slownik_wartosci.items():
        if wartosc == value:
            return key

def zastepowanie_stron ():
    licznik = 0
    zastapienie_strony = 0
    dozwolone_klucze = []

    for wartosc in lista_odwolan:

        ## FIFO ##
        if wartosc not in ramki_fifo:
            ramki_fifo[licznik] = wartosc
            licznik += 1
            zastapienie_strony += 1

            if licznik == max_ramek:
                licznik = 0

        ## LFU ##
        #if len(ramki) < max_ramek:
        #    if wartosc not in ramki:
        #        ramki.append(wartosc)
                #zastapienie_strony += 1
        #    slownik_wartosci[wartosc] += 1
        #    print(slownik_wartosci)
        #else:
        #    slownik_wartosci[wartosc] += 1
        #    if wartosc not in ramki:
        #        dozwolone_klucze.clear()
        #        for r in ramki:
        #           dozwolone_klucze.append(r)
        #        tmp_slownik = ({k:v for (k,v) in slownik_wartosci.items() if k in dozwolone_klucze})
        #        ofiara = min(tmp_slownik, key=tmp_slownik.get)
        #        index_ofiary = ramki.index(ofiara)
        #        zastapienie_strony += 1

        #        ramki[index_ofiary] = wartosc
    print("Zastapione strony: " + str(zastapienie_strony))
    #return ramki
    return ramki_fifo

print(zastepowanie_stron())




