pets = ['sola', 'zola', 'fasola']

while True:
    print('Podaj nazwę wierzaka: ')
    nazwa = input()
    if nazwa not in pets:
        print('sorry ale nie ma takiego zwierzaka')
    else:
        print('brawo tak ma na imię')