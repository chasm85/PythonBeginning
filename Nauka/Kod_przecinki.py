#  Zadanie: Utwórz funkcję pobierającą listę jako argument i zwracającą ciąg tekstowy wraz
#  z wszystkimi elementami rozdzielonymi przecinkiem i spacją, przy czym przed
#  ostatnim elementem powinien znajdować się spójnik i. Przykładowo po przeka-
#  zaniu funkcji powyższej listy spam powinna ona wygenerować następujące dane
#  wyjściowe: 'jabłka, banany, tofu i koty' . Oczywiście funkcja powinna mieć
#  możliwość pracy z dowolną przekazaną jej listą.

spam = ['jabłka', 'banany','tofu','koty']

def drukuj (listuj):
    for i in range(len(listuj)-2):
        print(listuj[i] +', ', end='')
    print(listuj[len(listuj)-2] +' ', end='')
    print('i ', end='')
    print(listuj[len(listuj)-1])

#test
drukuj(spam)