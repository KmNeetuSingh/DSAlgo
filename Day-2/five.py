# name = input()                  # Reading input from STDIN
# print('Hi, %s.' % name)         # Writing output to STDOUT
one, two , three , four , five = map(int, input().split())
sum1 = one+two
sum2 = three+four
if sum1 > five and sum2 > five :
  print("Yes")
else :
  print("No")