# x = list(range(5))
# # for item in x:
# #   print(item)

# # for item2 in (range(4)):
# #   print(item2)

# # print(len(x))

# # for i in range(len(x)):
# #   print (x[i])


# #deklaracja listy i interakcje 

# L=[3,5,8,13,17,27]

# for elem in L:
#   print (elem, end=" ")

# print("\n")

# for i in range(len(L)):
#   print (L[i], end=" ")
K = [4,7,5,7,3,3,2,8,7]
print(K)

# K.append(3)   #dodaje na koncu liczbe 3
# print(K)
# print(K.count(7))    #liczy ile jest 7
# print(K.index(7))    #pokazuje na ktorej pozycji jest pierwsza 7
# K.insert(2,4)
# print(K)
# #pytanie - jak wstawic "4" na koniec listy
# # K.insert(len(K),4)   #lub poprostu append
# # print(K)
# K.pop()   #pop() usuwa domyslnie ostatnia liczbe lub podana
# print(K)
# K.reverse()
# print(K)
# K.sort()   #lub sort(reverse=True) malejąco
# print(K)
# K.count(7)
# for i in range(K.count(7)):
#   K.remove(7)
# print(K)

for i in range(K.count(7)):
  K.pop(K.index(7))
print(K)

#poszukaj maxa w liscie

# print(max(K))
max = K[0]
for i in K:
  if i > max:
    maks = i
print(max)