

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'


def encrypt(message, key):
    translated = ''
    for symbol in message:
        if symbol in SYMBOLS:         
            translatedIndex = (SYMBOLS.find(symbol) + key) % 52
            translated = translated + SYMBOLS[translatedIndex]

        else:
            translated = translated + symbol
    return translated


with open("dracula.caesar.encrypted.txt", "w") as file2:
    with open("dracula.txt") as file1:
        message = file1.read()
        file2.write(encrypt(message, 8))
