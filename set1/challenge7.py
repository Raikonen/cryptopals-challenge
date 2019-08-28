import sys
import base64
from operator import itemgetter


def main():
    # Import encrpted text and decode
    with open("./ACB.txt", "r") as message_file:
        b64_ciphertext = message_file.read()
    ciphertext = base64.b64decode(b64_ciphertext)
    print(ciphertext)

if __name__ == "__main__":
    main()