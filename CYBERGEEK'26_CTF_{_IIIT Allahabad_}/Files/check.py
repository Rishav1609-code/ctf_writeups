# The given ciphertext
ciphertext = "0eRbrk{_ng}eoe3ZlaEm1g"

# Our mathematical constants
p = 23
g = 7

# Create an empty list of 23 elements (using 0-22 to handle 1-based indexing easily)
plaintext = [''] * p

# Loop through the ciphertext
for i, char in enumerate(ciphertext):
    # i is 0-indexed, so we add 1 to get the 1-based Ciphertext_Index
    cipher_idx = i + 1 
    
    # Calculate the original Plaintext_Index using the formula
    plain_idx = pow(g, cipher_idx, p)
    
    # Place the character in its correct original position
    plaintext[plain_idx] = char

# Join the list into a string, ignoring the empty 0th index
flag = "".join(plaintext[1:])

print(f"Decrypted Flag: {flag}")