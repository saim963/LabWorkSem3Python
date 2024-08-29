str = input("Enter a string: ")
pos = abs(int(input("Enter position from where you want to remove characters: ")))

def slice_str(stri,start):
    res = stri[:start]
    return res

result = slice_str(str,pos)
print(result)