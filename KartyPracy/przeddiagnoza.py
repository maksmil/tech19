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
# ALGORYTMY
print("ALGORYTMY")
# 1. Sprawdź czy wpisana przez usera liczba jest pierwsza
print("Zadanie 1")
liczba = int(input())
flaga = True
for i in range(2, liczba):
    if liczba % i:
        flaga = False
if flaga:
    print("Tak")
else:
    print("Nie")        
print()        

# 2. Sprawdź czy wpisana przez usera liczba jest złożona - liczba nie pierwsa
print("Zadanie 2")
liczba = int(input())
flaga = False
for i in range(2, liczba):
    if liczba % i:
        flaga = True
if flaga:
    print("Tak")
else:
    print("Nie")        
print()   

# 3. Sprawdź czy wpisana przez usera liczba jest względnie pierwsza z 24 - ich nwd to 1
print("Zadanie 3")
def nww(a, b):
    return a * b // nwd(a, b)

def nwd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a
    
    
liczba = int(input())
if nwd(liczba, 24) == 1:
    print("Tak")
else:
    print("Nie")


# 4. Zakoduj szyfrem CEZARA i kluczem k słowo s. - do nauczenia
print("Zadanie 4")
k = int(input("Klucz: "))
napis = input("Napis: ")
szyfr = ""
for i in range(len(napis)):
  szyfr += chr(65 + (ord(napis[i]) - 65 + k) % 26)
print(f"Napis: {napis} Szyfr: {szyfr}")
print()

# 5. Dodaj dwa ułamki a/b + c/d. Zapisz sumę jako ułamek nieskracalny i liczbę mieszaną.
print("Zadanie 5")
licznik1 = int(input("Licznik1: "))
mianownik1 = int(input("Mianownik1: "))
licznik2 = int(input("Licznik2: "))
mianownik2 = int(input("Mianownik2: "))

iloczyn = mianownik1 * mianownik2
wspolnyMianownik = iloczyn // nwd(mianownik1, mianownik2)

gotowyLicznik1 = (wspolnyMianownik // mianownik1) * licznik1
gotowyLicznik2 = (wspolnyMianownik // mianownik2) * licznik2

dodanyLicznik = gotowyLicznik1 + gotowyLicznik2

dzielnik = nwd(dodanyLicznik, wspolnyMianownik)
licznik = dodanyLicznik // dzielnik
mianownik = wspolnyMianownik // dzielnik

print(f"Ulamek nieskracalny: {licznik} / {mianownik}")
if licznik % mianownik == 0:
    print(f"Calosci: {licznik // mianownik}")
else:
    print(f"Calosci: {licznik // mianownik} i {licznik % mianownik} / {wspolnyMianownik}")
print()

# 6. Znajdź NWW dwóch wpisanych przez usera liczb

a = input()
b = input()
print(f"NWW: {nww(a, b)}")
print()

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