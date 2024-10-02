# Encryption and decryption
def encrypt_string(main_string, symbol):
    encrypted_string = ""
    for char in main_string:
        encrypted_string += char + symbol
    return encrypted_string

def decrypt_string(encrypted_string, symbol):
    decrypted_string = "".join(encrypted_string.split(symbol))
    return decrypted_string

main_string = input("Enter the main string to encrypt: ")
symbol = input("Enter the symbol to embed: ")

encrypted_string = encrypt_string(main_string, symbol)
print(f'Encrypted string: {encrypted_string}')

decrypted_string = decrypt_string(encrypted_string, symbol)
print(f'Decrypted string: {decrypted_string}')