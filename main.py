#-------------Dodawanie dwóch liczb-------------

#Liczba_1 = float(input("Podaj pierwszą liczbę: "))
#Liczba_2 = float(input("Podaj drugą liczbę: "))
#obliczenie = Liczba_1 + Liczba_2
#print("Wynik dodawania to:", obliczenie)

#-------------if-------------

#Liczba_1 = float(input("Podaj pierwszą liczbę: "))
#Liczba_2 = float(input("Podaj drugą liczbę: "))
#x = input("Wybierz działanie (+, -, *, /): ")

#if x == "+":
#    obliczenie = Liczba_1 + Liczba_2
#    print("Wynik dodawania to: ", obliczenie)
#elif x == "-":
#    obliczenie = Liczba_1 - Liczba_2
#    print("Wynik odejmowania to: ", obliczenie)
#elif x == "*":
#    obliczenie = Liczba_1 * Liczba_2
#    print("Wynik mnożenia to: ", obliczenie)
#elif x == "/":
#    if Liczba_2 == 0:
#        print("nie dziel przez zero")
#    else:
#        obliczenie = Liczba_1 / Liczba_2
#        print("Wynik dzielenia to: ", obliczenie)"


#-------------automatyczny kalkulator-------------


import re
#przykład wyrażenia: 5+5*25
while True:
    kalk = input("podaj wyrażenie matematyczne używając +, -, *, /: ")


    kalk = kalk.replace(",", ".")
    wyciaganie_liczb = re.split(r"[+\-\*\/]", kalk)
    wyciaganie_symboli = re.findall(r"[+\-\*\/]", kalk)

    czyste_liczby = []
    czyste_symbole = []

    for podzielone_liczby in wyciaganie_liczb:
        podzielone_liczby = float(podzielone_liczby)
        czyste_liczby.append(float(podzielone_liczby))


    for symbol in wyciaganie_symboli:
        if symbol != "":
            czyste_symbole.append(symbol)

    i = 0
    while i < len(czyste_symbole):
        symbol = czyste_symbole[i]
        if symbol == "*":
            wynik = czyste_liczby[i] * czyste_liczby[i+1]
            czyste_liczby[i] = wynik
            czyste_liczby.pop(i+1)
            czyste_symbole.pop(i)
        elif symbol == "/":
            wynik = czyste_liczby[i] / czyste_liczby[i+1]
            czyste_liczby[i] = wynik
            czyste_liczby.pop(i+1)
            czyste_symbole.pop(i)
        else:
            i += 1
    i = 0
    while i < len(czyste_symbole):
        symbol = czyste_symbole[i]
        if symbol == "+":
            wynik = czyste_liczby[i] + czyste_liczby[i+1]
            czyste_liczby[i] = wynik
            czyste_liczby.pop(i+1)
            czyste_symbole.pop(i)
        elif symbol == "-":
                wynik = czyste_liczby[i] - czyste_liczby[i+1]
                czyste_liczby[i] = wynik
                czyste_liczby.pop(i+1)
                czyste_symbole.pop(i)
        else:
            i += 1


    print("wynik to", czyste_liczby[0])