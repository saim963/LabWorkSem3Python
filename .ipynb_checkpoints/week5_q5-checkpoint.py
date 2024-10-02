#two lists with numbers; make new and add odd from list 1, even from list 2 to new list

lst1 = [1,2,3,4,5,6,7,8,9]
lst2 = [22,33,44,55,66,99,88,77,11]

lst = []
for i in lst1:
    if i%2!=0:  lst.append(i)
for i in lst2:
    if i%2==0:  lst.append(i)

print(lst)