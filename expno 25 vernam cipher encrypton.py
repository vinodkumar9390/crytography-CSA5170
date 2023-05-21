def vernam_encrypt(plaintext, key):
    ciphertext = ""
    for i in range(len(plaintext)):
       
        ciphertext += chr(ord(plaintext[i]) ^ ord(key[i]))
    return ciphertext


plaintext = input("Enter the plaintext: ")
key = input("Enter the key (must be the same length as plaintext): ")


if len(key) != len(plaintext):
    print("Error: The key length must be the same as the plaintext length.")
else:
    
    encrypted_text = vernam_encrypt(plaintext, key)
    print("Encrypted text:", encrypted_text)
