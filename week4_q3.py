def square_foo(lst):
    sq_lst = [x**2 for x in lst]
    return sq_lst

lst = []
n = int(input("Enter the length of the list: "))
for i in range(n):
    el = int(input(f"Element {i+1}: "))
    lst.append(el)
print("List: ",lst)
print("Squared list: ",square_foo(lst))