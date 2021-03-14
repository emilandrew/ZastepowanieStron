def LFU(slownik_wartosci, ramki, licznik):

    if licznik < max_ramek:
        ramki[licznik] = wartosc
        slownik_wartosci[wartosc] += 1
        licznik += 1

    else:
        wartosci = slownik_wartosci.values()
        lista_wartosci.clear()

        for w in wartosci:
            if w != 0:
                lista_wartosci.append(w)

        lista_wartosci.sort()
        min_num = lista_wartosci[0]

        klucz = get_key(min_num)
        # slownik_wartosci[klucz] = 0
        print(slownik_wartosci)
        print(lista_wartosci)

        if klucz in ramki:
            index_klucza = ramki.index(klucz)

            ramki[index_klucza] = wartosc

            slownik_wartosci[wartosc] += 1