list = []
temp = 0
num = abs(int(input("Enter a number: ")))
while num > 0:
    temp = num%10
    list.append(temp)
    num //= 10
print(list)