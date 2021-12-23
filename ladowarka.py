import sys
packages = 0        #liczba paczek wysłanych
kilos = 0        #suma kilogramów wysłanych
weight = 0.0          #waga elementu
box_weight = 0.0
print ('ładowarka paczek v0.9')
print ('podaj liczbę elementów do wysyłki')
items = int (input())
while items >0:
    print ('podaj wagę elementu')
    weight = float (input())
    if (weight == 0 or weight >10 or weight <1):
        break
    else:    
        if box_weight <=20:
            box_weight = box_weight+weight 
            kilos += weight
            print (kilos)
        else:  
            box_weight=0+weight 
            packages += 1
    items -= 1
if weight >10 or weight <1:
    print ('błąd')
else:
    print ('liczba paczek wysłanych {}' .format(packages))
    print ('liczba kilogramów wysłanych {}' .format(kilos))
    print ('suma pustych kilogramów {}' .format(packages*20-kilos))
    #print ('paczka numer {} miała najwięcej pustych kilogramów - {}kg' .format(box,20-box_weight))
