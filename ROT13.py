UNCYPHERED ="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
ROT13="NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
def rot13(message):
    ciphered_str = message.translate(message.maketrans(UNCYPHERED, ROT13))
    print(ciphered_str)

rot13(input("Ingresa un texto : "))
print("Saludos!")
