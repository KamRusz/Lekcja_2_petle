import sys
packages = 0        #liczba paczek wysłanych
kilos = 10.0        #suma pustych kilogramów
print ('ładowarka paczek v0.9')
print ('podaj liczbę elementów do wysyłki')
items = int (input())
while items >0:
    print ('podaj wagę elementu')
    waga = float (input())
    if waga == 0:
        break
    else:
        items -= 1
        packages += 1

print ('liczba paczek wysłanych {}' .format(packages))
print ('liczba kilogramów wysłanych {}' .format(kilos))
print ('suma pustych kilogramów {}' .format(packages*20-kilos))
#print ('paczka numer {} miała najwięcej pustych kilogramów - {}kg' .format(box,20-box_weight))

