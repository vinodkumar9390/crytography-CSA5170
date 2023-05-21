import string


def generate_matrix(key):
    
    key = key.replace(" ", "").upper()

    key = "".join(dict.fromkeys(key))

    
    matrix = list(key)

    alphabet = string.ascii_uppercase.replace("J", "")
    for letter in alphabet:
        if letter not in matrix:
            matrix.append(letter)

    return matrix


def generate_pairs(ciphertext):
  
    ciphertext = ciphertext.replace(" ", "").upper()

    pairs = []
    i = 0
    while i < len(ciphertext):
        pairs.append(ciphertext[i] + ciphertext[i + 1])
        i += 2

    return pairs


def decrypt(ciphertext, key):
    matrix = generate_matrix(key)
    pairs = generate_pairs(ciphertext)

    decrypted_message = ""
    for pair in pairs:
        letter1, letter2 = pair[0], pair[1]
        row1, col1 = divmod(matrix.index(letter1), 5)
        row2, col2 = divmod(matrix.index(letter2), 5)

        if row1 == row2:
            decrypted_message += matrix[row1 * 5 + (col1 - 1) % 5] + matrix[row2 * 5 + (col2 - 1) % 5]
        elif col1 == col2:
            decrypted_message += matrix[((row1 - 1) % 5) * 5 + col1] + matrix[((row2 - 1) % 5) * 5 + col2]
        else:
            decrypted_message += matrix[row1 * 5 + col2] + matrix[row2 * 5 + col1]

    return decrypted_message

key = "KEYWORD"
ciphertext = "EBIEBNBO"
decrypted_message = decrypt(ciphertext, key)
print("Decrypted message:", decrypted_message)
