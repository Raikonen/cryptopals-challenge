# Burning 'em, if you ain't quick and nimble
# I go crazy when I hear a cymbal
# Encrypt with key "ICE"
import sys

def main():
    message = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = b"ICE"
    ciphertext = repeating_key_XOR(message, key)
    print(ciphertext.hex())

def repeating_key_XOR(plaintext, key):
    output_bytes = b''
    index = 0
    for byte in plaintext:
        output_bytes += bytes([byte ^ key[index]])
        if(index + 1) == len(key):
            index = 0
        else:  
            index += 1
    return output_bytes


if __name__ == "__main__":
    main()