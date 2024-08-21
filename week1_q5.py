import math
num = int(input("Enter a number: "))
# cube till n
for n in range(1,num+1):
    print(f"{n}³= ",int(math.pow(n,3)))