import sys
import base64

# 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
def main():   
    hexstring = input()
    hexstring_to_b64(hexstring)

def hexstring_to_b64(string):
    decoded_hexstring = bytes.fromhex(string)
    print(decoded_hexstring)

    encoded_b64 = base64.b64encode(decoded_hexstring)
    print(encoded_b64)
    
    decoded_b64 = encoded_b64.decode()
    print(decoded_b64)

if __name__ == "__main__":
    main()