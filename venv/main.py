import numpy as np
from Scripts.menu import *

oferta = {}
listaKlienci = []
budzet = 50000

opcjeMenu = np.array([u'Dodaj lub usuń klienta', u'Wypisz klientów', u'Dodaj lub usuń produkt', u'Wypisz produkt', \
                       u'Dodaj lub usuń zamówienie', u'Wypisz zamówienia', u'Stan konta', u'Zakończ'])
opcjeMenuDod = np.array ([u'Dodaj',u'Usuń'])


while True:
    wybor = menuPrint(opcjeMenu)

    if wybor == 1:
        wybor = menuPrint(opcjeMenuDod)
        if wybor == 1:
            print(listaKlienci, '\n')
            nazwa = input('Nazwa: ')
            id = int(input('ID: '))
            miast = input('Miasto: ')
            listaKlienci.append((nazwa, id, miast))
            print(listaKlienci)
        if wybor == 2:
            print(listaKlienci)
            nr = int(input('Nr klienta: '))
            listaKlienci.pop(nr)
            print(listaKlienci)

    elif wybor == 2:
        print(listaKlienci)

    elif wybor == 3:
        wybor = menuPrint(opcjeMenuDod)
        if wybor == 1:
            print(oferta)
            nazwaPrzedmiot = input('Nazwa: ')
            cena = float(input('Cena: '))
            oferta[nazwaPrzedmiot] = cena
        if wybor == 2:
            print(oferta)
            nazwaPrzedmiot = input('Nazwa: ')
            oferta.pop(nazwaPrzedmiot)

    elif wybor == 4:
        print(oferta)

    elif wybor == 5:
        zamowienie =  {}
        wybor = menuPrint(opcjeMenuDod)
        if wybor == 1:
            wyb = input(u'Kontynuować? t/n')
            while wyb == 't':
                nr = int(input(u'Numer zamówienia: '))
                przedmiot = input('Nazwa: ')
                ilosc = int(input(u'Ilość:'))
                if przedmiot in oferta:
                    koszt = 0
                    cena = oferta[przedmiot]
                    koszt += (cena*ilosc)
                    zamowienie[nr] = (przedmiot,ilosc,cena*ilosc)
                    budzet += koszt
                    print(zamowienie)
                if przedmiot not in oferta:
                    print('Brak przedmiotu na stanie!')
                    pass
                wyb = input(u'Kontynuować? t/n')
        if wybor == 2:
            nr = int(input(u'Numer zamówienia: '))
            zamowienie.pop(nr)
            budzet = budzet - koszt

    elif wybor == 6:
        print(zamowienie)

    elif wybor == 7:
        print(budzet)

    elif wybor == 8:
        break
