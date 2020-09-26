import os

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'


def decrypt(cipher, key):
    translated = ''
    for symbol in cipher:
        if symbol in SYMBOLS:
            translatedIndex = (SYMBOLS.find(symbol) - key) % 52
            translated = translated + SYMBOLS[translatedIndex]

        else:
            translated = translated + symbol
    return translated


with open("dracula.caesar.decrypted.txt", "w") as file2:
    with open("dracula.caesar.encrypted.txt") as file1:
        message = file1.read()
        file2.write(decrypt(message, 8))