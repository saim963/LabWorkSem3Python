num = abs(int(input("Enter a number: ")))
sum =0
if num == 0:
   print("Number of digits: 1")
else:  
    temp =0
    while num > 0:
        temp = num%10
        sum += temp
        num = num // 10
    print(f"Number of digits: {sum}")