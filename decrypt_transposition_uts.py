import os
import math


def decrypt(message, key):
    numofcolumns = int(math.ceil(len(message)/float(key)))
    numofrows = key
    numofshadedboxes = (numofcolumns * numofrows) - len(message)

    plaintext = [''] * numofcolumns

    column = 0
    row = 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1

        if(column == numofcolumns) or (column == numofcolumns - 1 and row >= numofrows - numofshadedboxes):
            column = 0
            row += 1

    return ''.join(plaintext)


def main():
    with open("dracula.transposition.encrypted.txt") as file2:
        with open("dracula.transposition.decrypted.txt", "w") as file1:
            message = file2.read()
            file1.write(decrypt(message, 8))


if __name__ == "__main__":
    main()