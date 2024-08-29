# factorial of a given number 5! = 120 i.e-> 1*2*3*4*5
fac = 1
num = int(input("Enter a number: "))
if num == 0:    print(f"Factorial {num}: 1")
elif num<0:     print(f"Factorial {num}: Not defined")
else:
    for i in range(1,num+1):
        fac *= i
    print(f"Factorial {num}: {fac}")