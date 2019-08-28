import sys
from operator import itemgetter

# hex encoded string 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
# Key is 88

def main():
    # Create hexstring list
    char_strings_list = []
    with open('./char_strings.txt', 'r') as inputfile:
        for line in inputfile:
            char_strings_list.append(line.strip('\n').split(',')[0])

    letterfrequency = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }
    
    # For each hexstring in hexstring list, convert to bytestring, get the best bytestring and add an entry into top_list
    top_list = []
    counter = 1
    for char_string in char_strings_list:
        byte_string = bytes.fromhex(char_string)
        top_list.append(find_best_XORed_bytestring(counter, byte_string, letterfrequency))
        counter += 1

    # Sort to get the best of the best entry
    sorted_top_list = sorted(top_list, key = itemgetter('Score'), reverse=True)
    top_entry = sorted_top_list[0]

    # Print decoded message
    top_bytestring = char_strings_list[(top_entry['Entry Number']-1)]
    top_XOR_char = top_entry['XOR_char']
    print(XORed(bytes.fromhex(top_bytestring),top_XOR_char).decode("utf-8"))


# Return best bytestring as a dictionary entry of the bytestring and score
def find_best_XORed_bytestring(entry, byte_string, letterfrequency):
    bytestring_entry = {}
    score_dict = {}
    for i in range(256):
        score_dict[i] = score(XORed(byte_string, i), letterfrequency)
        sorted_d = sorted(score_dict.items(), key=itemgetter(1), reverse=True)
    bytestring_entry['Entry Number'] = entry
    bytestring_entry['XOR_char'] = sorted_d[0][0]
    bytestring_entry['Score'] = sorted_d[0][1]
    return bytestring_entry
    

def XORed(bytes1, bytes2):
    result = b''
    for b1 in bytes1:
        result += (bytes([b1 ^ bytes2]))
    return result
    
def score(bytestring, letterfrequency):
    score = 0
    for byte in bytestring.lower():
        score += letterfrequency.get(chr(byte), 0)
    return score

if __name__ == "__main__":
    main()