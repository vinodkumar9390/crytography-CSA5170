import string


def encrypt(plaintext, shift):
   
    plaintext = plaintext.replace(" ", "").upper()

    
    alphabet = string.ascii_uppercase
    n = len(alphabet)

    
    ciphertext = ""

    
    for letter in plaintext:
        if letter in alphabet:
          
            index = alphabet.index(letter)
            encrypted_index = (index + shift) % n
            encrypted_letter = alphabet[encrypted_index]
            ciphertext += encrypted_letter

    return ciphertext


def decrypt(ciphertext, shift):
   
    alphabet = string.ascii_uppercase
    n = len(alphabet)

   
    plaintext = ""

    for letter in ciphertext:
        if letter in alphabet:
           
            index = alphabet.index(letter)
            decrypted_index = (index - shift) % n
            decrypted_letter = alphabet[decrypted_index]
            plaintext += decrypted_letter

    return plaintext

plaintext = "HELLO WORLD"
shift = 3

encrypted_message = encrypt(plaintext, shift)
print("Encrypted message:", encrypted_message)

decrypted_message = decrypt(encrypted_message, shift)
print("Decrypted message:", decrypted_message)
