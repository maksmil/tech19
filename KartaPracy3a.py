# n = int(input())
# for i in range(n):
#   print("*-|", end=" ")

# #zad2
# n= int(input())
# for i in range(1, n+1):
#   print("*"*i, end="")
#   if i%2:
#     print("||", end="")
#   else:
#     print("--", end="")
# #zad 3
# n = int(input())
# for i in range(1, n+1):
#   print("*", end="")
#   if i % 2 ==1:
#     print("|"*i, end="")
#   else:
#     print("-"*i, end="")

for i in range(1,11):
  for j in range(1,11):
   print(i*j, end="\t")
  print()