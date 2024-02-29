

def caesar_encode(plain_text, shift):
    cipher_text = ""
    for c in plain_text:
        c_encoded = ord(c) + shift
        if c.islower():
            if c_encoded > ord('z'):
                c_encoded -= 26
        elif c.isupper():
            if c_encoded > ord('Z'):
                c_encoded -= 26
        c_encoded = chr(c_encoded)
        cipher_text += c_encoded
    return cipher_text
