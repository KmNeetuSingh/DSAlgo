# name = input()                  # Reading input from STDIN
# print('Hi, %s.' % name)         # Writing output to STDOUT
one, two , three, four , five = map(int, input().split())
ans = (one+two+three+four+five)*2
print(ans)