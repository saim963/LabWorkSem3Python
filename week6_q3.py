#  Enter a 4 digit number and sum sq of first and last two
def foo():
    num = input('Enter a 4 digit number: ')
    if len(num) !=4 :
        print('Try Again:')
        return foo()
        
    start = int(num[:2])
    end = int(num[2:])
    result = start*start + end*end
    print(f'Result squared sum: {result}')

foo()