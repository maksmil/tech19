#zad 1
suma = 0
for i in range(100, 1000):
    suma += i
print(suma)

#zad 2
suma = 0
for i in range(10,100):
    if i % 6 == 0:
        suma += i
print(suma)

#zad 3
from random import randint
losowe = []
for i in range(5): losowe.append(randint(1000, 10000))
print(f"{losowe} max: {max(losowe)}")

#zad4
liczba = input("Daj liczbę:")
suma = 0
for i in liczba:
    suma += int(i)
print(f"Suma to: {suma}")

#zad 5
liczba = input("Daj liczbę:")
Tab = []
for i in liczba:
    Tab.append(int(i))
print(f"Minimalna to: {min(Tab)}")

# ALGO

#zad 1
def CzyPierwsza(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

liczba = int(input("Daj liczbe:"))
if CzyPierwsza(liczba):
    print("Tak, Pierwsza")
else:
    print("Nie, Niepierwsza")

#zad 2
def CzyZlozona(x):
    for i in range(2,x):
        if x % i == 0:
            return True
    return False

liczba = int(input("Daj liczbe:"))
if CzyZlozona(liczba):
    print("Tak, Złożona")
else:
    print("Nie, Niezłożona")

#zad 3
from math import gcd
liczba = int(input("Daj liczbe:"))
if gcd(liczba,24) == 1:
    print("Tak, Względnie pierwsza z 24")
else:
    print("Nie, Niewzględnie pierwsza z 24")

#zad 4
napis = input("Podaj napis do szyfracji: ")
szyfr = ""
klucz = int(input("Podaj klucz: "))

for i in range(len(napis)):
    szyfr = szyfr + chr(65 + (ord(napis[i]) - 65 + klucz) % 26)
print("Szyfracja:", szyfr)

#zad 5
from math import gcd, lcm

goraA = int(input("GoraA:"))
dolA = int(input("DolA:"))
goraB = int(input("GoraB:"))
dolB = int(input("DolB:"))

nww = lcm(dolA, dolB)
wynik1 = (nww // dolA) * goraA
wynik2 = (nww // dolB) * goraB

print(wynik1 + wynik2, "/", nww)


print("NAPISY")
# 1. Znajdź ilość liter C we wpisanym napisie
print("Zadanie 1")
napis = input()
ile = 0
for i in napis:
    if i == "C":
        ile += 1
print(f"C wystepuje w napisie: {ile} razy")
print()

# 2. Sprawdź czy literki w napisie są w porządku nierosnącym: np ZOO, WOK, WODA itp
print("Zadanie 2")
napis = input()
napisCheck = list(napis)
napisCheck.sort()
napisCheck.reverse()

if list(napis) == napisCheck:
    print("Tak")
else:
    print("Nie")
print()

# 3. Podaj najdłuższy z 3 wpisanych przez usera wyrazów.
print("Zadanie 3")
maks = 0
nazwy = []
for i in range(3):
    napis = input()
    if len(napis) > maks:
        maks = len(napis)
        nazwy.append(i + 1)
print(f"Jest to slowo numer {nazwy[len(nazwy) - 1]}")