import os


def main():

    def encrypt(message, key):
        ciphertext = [''] * key

        for col in range(key):
            pointer = col

            while pointer < len(message):
                ciphertext[col] += message[pointer]

                pointer += key
        return ''.join(ciphertext)

    with open("dracula.transposition.encrypted.txt", "w") as file2:
        with open("dracula.txt") as file1:
            message = file1.read()
            file2.write(encrypt(message, 8))


if __name__ == "__main__":
    main()