# name = input()                  # Reading input from STDIN
# print('Hi, %s.' % name)         # Writing output to STDOUT
one , two , three , four , five , six = map(int, input().split())
two , five ,six = two*2 , six*2 , five*2
three , four = three*3 , four*3
sum = (one+ two+three+ four+five+six)
print(sum)



# print(one)
