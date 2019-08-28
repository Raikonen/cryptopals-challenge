import sys
# 1c0111001f010100061a024b53535009181c
# 686974207468652062756c6c277320657965

def main():   
    hexstring1 = '1c0111001f010100061a024b53535009181c'
    hexstring2 = '686974207468652062756c6c277320657965'
    decoded_hexstring1 = bytes.fromhex(hexstring1)
    decoded_hexstring2 = bytes.fromhex(hexstring2)
    print(decoded_hexstring1)
    print(decoded_hexstring2)
    print(XOR_hexstrings(decoded_hexstring1,decoded_hexstring2))

def XOR_hexstrings(bytes1, bytes2):
    result = b''
    for b1, b2 in zip(bytes1, bytes2):
        print(b1)
        result += (bytes([b1 ^ b2]))
    return result
if __name__ == "__main__":
    main()