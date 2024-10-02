def foo():
    phone_book = {'Saim':9536944109,'Areeb':9520916526,'Raim':9368055658}
    name = input('Enter a name to search in the dictionary: ')
    if  name in phone_book: print(f'Name: {name} => {phone_book[name]}')
    else:   print('No such user found!!')

foo()
foo()