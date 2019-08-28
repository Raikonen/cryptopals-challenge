import sys
import base64
from operator import itemgetter

def main():
    # Import encrpted text and decode
    with open("./encryptedb64.txt", "r") as message_file:
        b64_ciphertext = message_file.read()
    ciphertext = base64.b64decode(b64_ciphertext)
    letterfrequency = {
    'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
    'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
    'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
    'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
    'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
    'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
    'y': .01974, 'z': .00074, ' ': .13000
    }
    # Get results for different keysizes
    average_distances = []
    distances = []
    for keysize in range(2,41):
        chunks = get_chunks(ciphertext, keysize)
        while True:
            try:
                chunk_1 = chunks[0]
                chunk_2 = chunks[1]
                distance = find_distance(chunk_1, chunk_2)
                # Normalize this result by dividing by KEYSIZE
                distances.append(distance/keysize)

                # Remove these chunks so when the loop starts over, the
                # Hamming distance for the next two chunks can be calculated
                del chunks[0]
                del chunks[1]

                # When an exception occurs (indicating all chunks have 
                # been processed) break out of the loop.
            except Exception:
                break

        result = {
            'Key': keysize,
            'Average Distance': sum(distances) / len(distances)
            }
        average_distances.append(result)

    # Get top 3 results
    top_3_keysizes = []
    sorted_average_distance = sorted(average_distances, key=lambda x: x['Average Distance'])
    for i in range(3):
        top_3_keysizes.append(sorted_average_distance[i])
    
    for keysize in top_3_keysizes:
        test_keysize = keysize["Key"]


        # Break ciphertext into blocks
        blocks = get_chunks(ciphertext, test_keysize)

        # Transpose the blocks
        transposed_blocks_list = []

        # Create transposed bytestrings
        # Iterate through number of bytes in a blocks
        print(test_keysize, end="\n")
        for i in range(1, test_keysize+1):
            transposed_block = b''
            # Iterate through number of blocks
            for j in range(len(blocks)):
                byte = blocks[j][i-1:i]
                transposed_block = transposed_block + byte
            transposed_blocks_list.append(transposed_block)

        # Single Char XOR for each block in the transposed block list
        top_list = []
        for block in transposed_blocks_list:
            top_list.append(find_best_XORed_bytestring(block, letterfrequency))

        # Generate repeating key
        repeating_key = ""
        for entry in top_list:
            repeating_key = repeating_key + chr(entry['XOR_char'])
        print(repeating_key)


def get_chunks(ciphertext, keysize):
    chunks_list = []
    for i in range(0, len(ciphertext), keysize):
        chunks_list.append(ciphertext[i:i+keysize])
    return(chunks_list)

def find_distance(bytestring1, bytestring2):
    total_diff = 0
    for b1, b2 in zip(bytestring1, bytestring2):
        diff = b1 ^ b2
        for bit in bin(diff):
            if(bit == '1'):
                total_diff += 1
    return total_diff

def find_best_XORed_bytestring(byte_string, letterfrequency):
    bytestring_entry = {}
    score_dict = {}
    for i in range(256):
        score_dict[i] = score(XORed(byte_string, i), letterfrequency)
        sorted_d = sorted(score_dict.items(), key=itemgetter(1), reverse=True)
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