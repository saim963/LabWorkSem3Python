# num 1234 sum of digits at odd and even
e = 0
o = 0
num = input("Enter a number: ")
for i in num:
    i = int(i)
    if i%2==0:
        e+=i
    else:
        o+=i

print(f"Even: {e}, Odd: {o}")