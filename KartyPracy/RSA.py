#PRE
from math import gcd
print(gcd(12,16))

#1. wybor 2  duzych liczb pierwszych
p = 11
q = 13

#2.stworzenie funkcji F = (p-1) * (q-1) i znalezienie n = p * q
F = (p - 1) * (q - 1)
n = p * q
print(n)
print(F)

#3. Znalezienie klucza publicznego e: NWD(F, e) = 1
from math import gcd
for i in range(2,F):
  if gcd(i, F) == 1:
    e = i
    break
print(e)

#4. wygenerowanie klucza prywatnego d: d*e mod n = 1
for i in range(2,n):
  if (i*e) % F == 1:
    d = i
    break
print(d,n)

#przyklad dzialania:
#c = x**e mod n (szyfrogram)
#t = c**d mod n (na teks jawny)

msg = input()
szyfrogram = ""
for i in msg:
  szyfrogram += (chr((ord(i)**e) % n))
print(szyfrogram)

jawny = ""
for j in szyfrogram:
  jawny += chr((ord(j)**d)%n)
print(jawny)