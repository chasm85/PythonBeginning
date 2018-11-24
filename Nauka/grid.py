# Przyjmujemy założenie o istnieniu listy list, gdzie każda wartość wewnętrznej listy to ciąg tekstowy składający się z
# pojedynczego znaku, jak pokazałem poniżej. Wywołanie grid[x][y] możesz potraktować jako znak o współrzędnych X i Y
# „obrazu” narysowanego na podstawie znaków przechowywanych przez grid .

# Punkt o współrzędnych (0, 0) znajduje się w lewym górnym rogu, wartość współrzędnych X zwiększa się w prawą stronę,
# natomiast współrzędnych Y zwiększa się w dół. Utwórz kod, który na podstawie przedstawionej powyżej wartości grid
# utworzy następujący obraz.
# ..OO.OO..
# .OOOOOOO.
# .OOOOOOO.
# ..OOOOO..
# ...OOO...
# ....O....
# Podpowiedź. Konieczne będzie użycie pętli w pętli, aby wyświetlić znak o współrzędnych grid[0][0] , później grid[1][0]
# następnie grid[2][0] i tak dalej aż do grid[8][0] . W ten sposób powstanie pierwszy wiersz obrazu, po którym należy
# umieścić znak nowego wiersza. Teraz program powinien wyświetlić znak o współrzędnych grid[0][1] , później grid[1][1]
# następnie grid[2][1] i tak dalej. Ostatni znak wyświetlony przez program będzie miał współrzędne grid[8][5] .
# Pamiętaj również o przekazaniu funkcji print() argumentu w postaci słowa kluczowego end , jeśli nie chcesz otrzymać
# znaku nowego wiersza umieszczanego automatycznie po każdym wywołaniu print()


grid = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['.', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.']]

for y in range(6):
    for x in range(9):
        print(grid[x][y], end='')
    print('\n')
