# Napisz program "reader.py", który zmodyfikuje plik csv i wyświetli
# w terminalu jego zawartość, a następnie zapisze w wybranej lokalizacji.
# Wykonanie programu:

# reader.py <src> <dst> <change1> <change2> ..
# src to ścieżka pliku csv. Jeśli plik nie istnieje bądź podana ścieżka nie jest
# plikiem, wyświetl błąd i wskaż pliki w tym samym katalogu.
# dst to docelowa ścieżka, w której zapiszemy zmieniony plik csv.

# change1 ... changeN to ciągi znaków w posraci "Y,X,wartosc" Y to wiersz do zmodyfikowania
# (liczony od 0, X to kolumna (liczona od 0).
# Komórka pod wskazanym adresem powinna zmienić wartość na "wartosc"

import sys

class CsvReader:
    def __init__(self):
        self.input_file = sys.argv[1]
        self.output_file = sys.argv[2]
        self.task = []
        for row in sys.argv[3:]:
            self.task.append(row)
    def read_file(self):
        lines = []
        with open("plik.csv", "r", encoding='utf-8') as file:
            for line in file.readlines():
                tmp = line.split('\n')[0].split(',')
                lines.append(tmp)
            print(lines)

        return lines

    def change_file(self):
        for change in self.task:


read = CsvReader()
read.read_file()