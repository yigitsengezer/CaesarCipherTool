import argparse

parser = argparse.ArgumentParser(description='Crypt or decrypt a text with Caesar Cipher.')
parser.add_argument('-c', '--crypt', help='Text to crypt.', required=False)
parser.add_argument('-d', '--decrypt', help='Text to decrypt.', required=False)
parser.add_argument('-k', '--key', help='Key to crypt.', type=int, required=False)
args = parser.parse_args()


def caesar_cipher(text, key):
    crypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                crypted_text += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
            else:
                crypted_text += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        else:
            crypted_text += char
    return crypted_text

def caesar_decipher(text, key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                decrypted_text += chr((ord(char) - ord('A') - key) % 26 + ord('A'))
            else:
                decrypted_text += chr((ord(char) - ord('a') - key) % 26 + ord('a'))
        else:
            decrypted_text += char
    return decrypted_text


if __name__ == '__main__':
    
    if args.crypt:
        plainText = args.crypt
    elif args.decrypt:
        plainText = args.decrypt
    else:
        plainText = input("Enter text to crypt or decrypt: ")

    if args.key:
        key = args.key
    else:
        key = int(input("Enter key: "))

    if args.crypt:
        encryptedText = caesar_cipher(plainText, key)
        print("Encrypted text: " + encryptedText)
    elif args.decrypt:
        decryptedText = caesar_decipher(plainText, key)
        print("Decrypted text: " + decryptedText)
    else:
        isCrypt = input("Do you want to crypt or decrypt? (C/d): ")
        if isCrypt == "c" or isCrypt == "C" or isCrypt == "":
            encryptedText = caesar_cipher(plainText, key)
            print("Encrypted text: " + encryptedText)
        else:
            decryptedText = caesar_decipher(plainText, key)
            print("Decrypted text: " + decryptedText)