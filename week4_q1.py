def cal_sum_sub(a,b):
    sum = a+b
    diff = (a-b) if a>b else (b-a)
    return (sum,diff)

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
result = cal_sum_sub(a,b)
print("The sum and difference are as follows: ",result)