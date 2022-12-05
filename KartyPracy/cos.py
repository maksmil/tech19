# #funkcja ord() - zwraca kod ascii dla danego znaku
# print(ord("A"))
# print(ord("B"))
# print(ord("C"))

# #funkcja chr() - zawsze znak dla danego kodu ascii
# print(chr(65))
# print(chr(75))
# print(chr(85))

# #mozna laczyc
# print(chr(ord("C")))
# print(chr(ord("C")+1))
# for i in range(65,91):
#   print(chr(i), end="")

#jak wydobyc literki z napisu...
# napis = "POLSKA"
# print(len(napis))
# print(napis[0])
# print(napis[1])

# #napisz petle wyciagajaca z napisu literki

# napis = input()
# #tutaj mozna dac napis = napis.replace(" ","") wtedy wypisze bez spacji
# for i in range(len(napis)):
#   print(napis[i])

# #napisz petle wyciagajaca kody ascii z napisow

# napis = input()
# for i in range(len(napis)):
#   print(ord(napis[j]))

# # #zaszyfruj napis Cezarem w kluczu = 3

# napis = input()
# szyfr = ""
# for i in range(len(napis)):
#   szyfr = szyfr + chr(ord(napis[i])+3)
# print(napis, szyfr)