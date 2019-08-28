import sys
from operator import itemgetter

# hex encoded string 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
# Key is 88

def main():   
    hexstring = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    bytestring = bytes.fromhex(hexstring)


    letterfrequency = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }

    potentialmessagedict = {}
    for i in range(256):
        potentialmessagedict[i] = scoring(XORed(bytestring, i), letterfrequency)
    sorted_d = sorted(potentialmessagedict.items(), key=itemgetter(1), reverse=True)
    print("Number 1: {0}".format(sorted_d[0]))
    print("Number 2: {0}".format(sorted_d[1]))
    print("Number 3: {0}".format(sorted_d[2]))

def XORed(bytes1, bytes2):
    result = b''
    for b1 in bytes1:
        result += (bytes([b1 ^ bytes2]))
    return result
    
def scoring(bytestring, letterfrequency):
    score = 0
    for byte in bytestring.lower():
        score += letterfrequency.get(chr(byte), 0)
    return score

if __name__ == "__main__":
    main()