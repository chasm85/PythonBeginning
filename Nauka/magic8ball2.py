import random

messages=  ['To pewne',
            'Zdecydowanie tak',
            'Tak',
            'Niejasna odpowiedź, spróbuj ponownie',
            'Zapytaj ponownie',
            'Skoncentruj się i zapytaj ponownie',
            'Moja odpowiź brzmi nie',
            'To nie wygląda zbyt dobrze',
            'Bardzo wątpliwe']

print(messages[random.randint(0,len(messages)-1)])