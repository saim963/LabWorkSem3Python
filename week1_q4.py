num = int(input("Enter a number: "))

def reverse(num):
    rev_num = 0
    while num!= 0:
        digit = num % 10
        rev_num = rev_num*10 + digit
        num //= 10
    return rev_num

def main():
    num_rev = reverse(num)
    if num == num_rev:
        print(f"{num} is a palindrome.")
    else:
        print(f"{num} is not a palindrome.")

main()