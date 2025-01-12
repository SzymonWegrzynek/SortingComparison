# Zestawienie czasu sortowań w Pythonie

## Opis projektu

Praca domowa polega na napisaniu kodu w Pythonie generującego zestawienie czasu sortowań poszczególnych algorytmów.
Dla danych trzech prób danych o rozmiarach odpowiednio 100, 1000, 10000 będą uruchamiane algorytmy.
Sposób generowania danych ma znaczenie i może mieć wpływ na ocenę.
Funkcja licząca czas ma przyjmować w parametrach funkcję sortującą i daną listę liczb.
Czasy sortowań są zaokrąglone do 3 miejsc po przecinku.

## Algorytmy sortujące

1. Bubble Sort
2. Insertion Sort
3. Quick Sort
4. Merge Sort
5. TimSort
6. IntroSort
7. Sort in Python

## Struktura tabeli wyników

```
Rozmiar danych | Bubble Sort | Insertion Sort | Quick Sort | Merge Sort | TimSort | IntroSort | Sort in Python
---------------------------------------------------------------------------------------------------------------
100            | 0.002 s     | 0.001 s        | 0.000 s    | 0.000 s    |   ...   |           |
1000           | 0.150 s     | 0.120 s        | 0.010 s    | 0.008 s    |         |           |
10000          | 15.470 s    | 11.230 s       | 0.120 s    | 0.100 s    |         |           |
```
