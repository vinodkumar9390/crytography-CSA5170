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


def generate_pairs(message):
    
    message = message.replace(" ", "").upper()

    pairs = []
    i = 0
    while i < len(message):
        if i == len(message) - 1 or message[i] == message[i + 1]:
            pairs.append(message[i] + "X")
            i += 1
        else:
            pairs.append(message[i] + message[i + 1])
            i += 2

    return pairs


def encrypt(message, key):
    matrix = generate_matrix(key)
    pairs = generate_pairs(message)

    encrypted_message = ""
    for pair in pairs:
        letter1, letter2 = pair[0], pair[1]
        row1, col1 = divmod(matrix.index(letter1), 5)
        row2, col2 = divmod(matrix.index(letter2), 5)

        if row1 == row2:
            encrypted_message += matrix[row1 * 5 + (col1 + 1) % 5] + matrix[row2 * 5 + (col2 + 1) % 5]
        elif col1 == col2:
            encrypted_message += matrix[((row1 + 1) % 5) * 5 + col1] + matrix[((row2 + 1) % 5) * 5 + col2]
        else:
            encrypted_message += matrix[row1 * 5 + col2] + matrix[row2 * 5 + col1]

    return encrypted_message


key = "KEYWORD"
message = "HELLO WORLD"
encrypted_message = encrypt(message, key)
print("Encrypted message:", encrypted_message)
