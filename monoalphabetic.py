from numpy import random
import pprint

ALPHABET_LOWER = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHABET_LENGTH = 26
START_VAL_LOWER = 97
START_VAL_UPPER = 65

alphabet_frequencies = [ 
    {"letter": "A", "frec": 8.167}, {"letter": "B", "frec": 1.492}, {"letter": "C", "frec": 2.782}, {"letter": "D", "frec": 4.253}, 
    {"letter": "E", "frec": 12.702}, {"letter": "F", "frec": 2.228}, {"letter": "G", "frec": 2.015}, {"letter": "H", "frec": 6.094}, 
    {"letter": "I", "frec": 6.996}, {"letter": "J", "frec": 0.153}, {"letter": "K", "frec": 0.772}, {"letter": "L", "frec": 4.025}, 
    {"letter": "M", "frec": 2.406}, {"letter": "N", "frec": 6.749}, {"letter": "O", "frec": 7.507}, {"letter": "P", "frec": 1.929}, 
    {"letter": "Q", "frec": 0.095}, {"letter": "R", "frec": 5.987}, {"letter": "S", "frec": 6.327}, {"letter": "T", "frec": 9.056}, 
    {"letter": "U", "frec": 2.758}, {"letter": "V", "frec": 0.978}, {"letter": "W", "frec": 2.360}, {"letter": "X", "frec": 0.150}, 
    {"letter": "Y", "frec": 1.974}, {"letter": "Z", "frec": 0.074}
]

pp = pprint.PrettyPrinter(indent=4)

def main():
    print("--------MONOALPHABETIC ENCRYPTION----------")
    ciphered_text = monoalphabetic_cipher("ATTACKATONCE")
    print("Ciphered Text: ", ciphered_text)
    print()

    alphabet_sorted = sorted(alphabet_frequencies, key=lambda k: k['frec'], reverse=True)
    pp.pprint(alphabet_sorted)

    print("\n\n--------MONOALPHABETIC DECRYPTION----------")
    pp.pprint(monoalphabetic_decription(ciphered_text))


def monoalphabetic_cipher(text):
    alphabet_array = str_to_array(ALPHABET_UPPER)
    perm = random.permutation(alphabet_array)
    ciphered_text = ""

    print("Alphabet: ", alphabet_array)
    print("Permutation: ", perm)
    print("Original Text: ", text)

    for c in text:
        char_index = get_letter_index(c, alphabet_array)
        # print("Letter: ", c, " Index: ", char_index)

        ciphered_text += perm[char_index]


    return ciphered_text

def monoalphabetic_decription(text):
    text_array = str_to_array(text)
    length = len(text_array)
    text_frec = []

    print("Ciphered Text: ", text)

    for i in range(length):
        # print("Char: ", text_array[i])

        item_index = contains_letter(text_frec, text_array[i])

        # print("index: ", item_index)

        if(item_index == -1):
            text_frec.append({
                "letter": text_array[i],
                "frec": 1
            })
        else:
            text_frec[item_index]["frec"] += 1

    return text_frec

def contains_letter(text_dictionary, letter):
    if not text_dictionary:
        return -1

    indx = 0 

    for item in text_dictionary:
        # print(item)

        if(letter == item["letter"]):
            return indx
        
        indx += 1
        
    
    return -1

def str_to_array(text):
    array = []

    for c in text:
        array.append(c)
    
    return array

def get_letter_index(letter, alphabet):
    length = len(alphabet)

    index = -1

    for i in range(length):
        if(letter == alphabet[i]):
            index = i
    
    return index

if __name__ == "__main__":
    main()