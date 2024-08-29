# num 1234 sum of digits at odd and even
sum_even = 0
sum_odd=0
count= 0
num = int(input("Enter a number: "))
while num:
    digit = num%10
    num//=10
    if count%2==0:
        sum_odd=sum_odd+digit
    if count%2!=0:
        sum_even+sum_even+digit
    count+=1


print(sum_even,sum_odd)