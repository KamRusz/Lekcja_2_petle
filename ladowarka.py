import sys
packages = 0            #liczba paczek wysłanych
kilos = 0               #suma kilogramów wysłanych
weight = 0.0            #waga elementu
box_weight = 0.0        #waga paczki
max_empty_box_weight = 0
max_empty_box_number = 0
print ('ładowarka paczek v0.9')
print ('podaj liczbę elementów do wysyłki')
items = int (input())
while items > 0:
    print ('podaj wagę elementu')
    weight = float (input())
    if (weight == 0 or weight > 10 or weight < 1):
        break   
    if box_weight + weight <= 20:
            box_weight += weight 
            kilos += weight
            print (kilos)
    else:  
        empty_box_weight = 20 - box_weight
        box_weight = 0 
        box_weight= weight 
        kilos += weight
        packages += 1
        print (kilos)
        if empty_box_weight > max_empty_box_weight:
            max_empty_box_number = packages
            max_empty_box_weight = empty_box_weight
    items -= 1
if weight > 10 or (weight < 1 and weight!= 0):
    print ('błąd')
else:
    if box_weight:
        empty_box_weight = 20 - box_weight
        packages += 1
        if empty_box_weight > max_empty_box_weight:
            max_empty_box_number = packages
            max_empty_box_weight = empty_box_weight
    print ('liczba paczek wysłanych {}' .format(packages))
    print ('liczba kilogramów wysłanych {}' .format(kilos))
    print ('suma pustych kilogramów {}' .format(packages * 20 - kilos))
    print ('paczka numer {} miała najwięcej pustych kilogramów - {}kg' .format(max_empty_box_number ,max_empty_box_weight))
