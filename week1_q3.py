input_string = input("Enter 20 numbers separated by 'space': ")
numbers = input_string.split()
numbers = [int(num) for num in numbers]
print(numbers)

print("Numbers divisible by 5: ")
for num in numbers:
    if num%5 == 0:
        print(num)