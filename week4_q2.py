def checker(lst):
    if len(lst) == 0:
        return False
    return lst[0] == lst[-1]

lst = []
n = int(input("Enter length of the list: "))
for i in range(n):
    element = int(input(f"Element {i+1}: "))
    lst.append(element)
print("Is the first and last element same in list: ",checker(lst))