def generate_playfair_key_matrix(key):
    key = ''.join(sorted(set(key), key=key.index)).replace('J', 'I')
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = []

    for char in key:
        if char not in matrix:
            matrix.append(char)

    for char in alphabet:
        if char not in matrix:
            matrix.append(char)
    
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return (i, row.index(char))
    return None

def playfair_encrypt(plaintext, key):
    matrix = generate_playfair_key_matrix(key)
    plaintext = plaintext.upper().replace('J', 'I')
    plaintext = ''.join([char for char in plaintext if char.isalpha()])

    if len(plaintext) % 2 != 0:
        plaintext += 'X'
    
    ciphertext = ''
    for i in range(0, len(plaintext), 2):
        a, b = plaintext[i], plaintext[i+1]
        if a == b:
            b = 'X'
        
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5]
            ciphertext += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1]
            ciphertext += matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2]
            ciphertext += matrix[row2][col1]
    
    return ciphertext

def playfair_decrypt(ciphertext, key):
    matrix = generate_playfair_key_matrix(key)
    ciphertext = ciphertext.upper().replace('J', 'I')
    
    plaintext = ''
    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i+1]
        
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:
            plaintext += matrix[row1][(col1 - 1) % 5]
            plaintext += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += matrix[(row1 - 1) % 5][col1]
            plaintext += matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += matrix[row1][col2]
            plaintext += matrix[row2][col1]
    
    return plaintext

key = "BLOCK"
plaintext = input("Enter the plaintext (without spaces): ").upper().replace('J', 'I')

ciphertext = playfair_encrypt(plaintext, key)
print(f"Ciphertext: {ciphertext}")

decrypted_text = playfair_decrypt(ciphertext, key)
print(f"Decrypted Text: {decrypted_text}")
