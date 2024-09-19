def checker(list):
    return list[0] == list[len(list)-1]

lst = []
n = int(input("Enter length of the list: "))
for i in range(0,n):
    lst.append(i)
print("Is the first and last element same in list: ",checker(lst))