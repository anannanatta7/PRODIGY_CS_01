def encrypt(text, shift):
    result = ""
    # traverse text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# Get user input
choice = input("Do you want to encrypt or decrypt the message? (e/d): ").lower()
if choice not in ['e', 'd']:
    print("Invalid choice")
else:
    text = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    if choice == 'e':
        print("Encrypted message:", encrypt(text, shift))
    elif choice == 'd':
        print("Decrypted message:", decrypt(text, shift))
