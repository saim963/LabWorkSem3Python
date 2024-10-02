def str_checker():
    sentence = input('Enter a sentence: ')
    upper_count = 0 
    lower_count = 0 
    alpha_count = 0 
    digit_count = 0
    for e in sentence:
        if e.isupper(): upper_count +=1
        if e.islower(): lower_count +=1
        if e.isalpha(): alpha_count +=1
        if e.isdigit(): digit_count +=1

    print(f'Number of uppercase characters: {upper_count}')
    print(f'Number of lowercase characters: {lower_count}')
    print(f'Number of alphabets: {alpha_count}')
    print(f'Number of digits: {upper_count}')

str_checker()