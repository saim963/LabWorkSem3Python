n = abs(int(input("Enter a number: ")))

for i in range(0,n):
    for j in range(0,i):
        print("*",end=" ")
    print()

for i in range(n,0,-1):
    for j in range(i,0,-1):
        print("*",end=" ")
    print()