import random
liczba = random.randint(1,20)
print('Mam na myśli pewną liczbę z zakresu 1 do 20')

for proba in range(1,6):
    print('Spróbuj odgadnąć liczbę')
    zgadnij = int(input())
    if zgadnij < liczba:
        print('Podana liczba jest za mała')
    elif zgadnij > liczba:
        print('Podana liczba jest za duża')
    else:
        break

if zgadnij == liczba:
    print('Doskonale odgadłeś liczbę podczas: ' + str(proba) + 'prób')
else:
    print('Nie udało się. Liczbę którą miałem na myśli to ' + str(liczba))