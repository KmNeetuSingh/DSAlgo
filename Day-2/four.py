# name = input()                  # Reading input from STDIN
# print('Hi, %s.' % name)         # Writing output to STDOUT
one , two , three , four = map(int, input().split())
if one > two  or three > four :
  print("Yes")
else :
  print("No")