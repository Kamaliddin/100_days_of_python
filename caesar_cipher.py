alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt the message or type 'decode' to decrypt the message.\n")
message = input('Type your message: ').lower()
shift = int(input('What is the shift: '))
def encrypt(text, shift):
    new_text = ''
    for letter in text:
        new_text += alphabet[alphabet.index(letter) + shift]
        
    return new_text

print(encrypt(message, shift))