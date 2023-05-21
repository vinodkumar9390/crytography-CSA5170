import string


def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def encrypt(plaintext, a, b):
   
    plaintext = plaintext.replace(" ", "").upper()

    
    alphabet = string.ascii_uppercase
    n = len(alphabet)

    
    ciphertext = ""

   
    for letter in plaintext:
        if letter in alphabet:
           
            index = alphabet.index(letter)
            encrypted_index = (a * index + b) % n
            encrypted_letter = alphabet[encrypted_index]
            ciphertext += encrypted_letter

    return ciphertext


def decrypt(ciphertext, a, b):
   
    alphabet = string.ascii_uppercase
    n = len(alphabet)

    
    a_inverse = mod_inverse(a, n)
    if a_inverse is None:
        raise ValueError("'a' does not have a modular multiplicative inverse.")

   
    plaintext = ""

   
    for letter in ciphertext:
        if letter in alphabet:
             
            index = alphabet.index(letter)
            decrypted_index = (a_inverse * (index - b)) % n
            decrypted_letter = alphabet[decrypted_index]
            plaintext += decrypted_letter

    return plaintext


plaintext = "HELLO WORLD"
a = 5
b = 8

encrypted_message = encrypt(plaintext, a, b)
print("Encrypted message:", encrypted_message)

decrypted_message = decrypt(encrypted_message, a, b)
print("Decrypted message:", decrypted_message)
