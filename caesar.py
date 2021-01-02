ALPHABET_LOWER = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHABET_LENGTH = 26
START_VAL_LOWER = 97
START_VAL_UPPER = 65

def main():
    print("-----------CAESAR ENCRYPTION--------------------\n")
    print("-----------UPPERCASED LETTERS------------------")
    print(caesar_cipher("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 23))
    print(caesar_cipher("ATTACKATONCE", 4))

    print("\n---------LOWERCASED LETTERS--------------------")
    print(caesar_cipher("abcdefghijklmnopqrstuvwxyz", 23))
    print(caesar_cipher("attackatonce", 4))

    print("\n------------MIXED LETTERS---------------------")
    print(caesar_cipher("ATTACKatonce", 4))

    print("\n\n-----------CAESAR DECRYPTION--------------------")
    print("-----------UPPERCASED LETTERS------------------")
    caesar_decryption("EXXEGOEXSRGI")

    print("\n---------LOWERCASED LETTERS--------------------")
    caesar_decryption("exxegoexsrgi")

    print("\n------------MIXED LETTERS---------------------")
    caesar_decryption("EXXEGOexsrgi")


def caesar_cipher(text, key):
    length = len(text)
    ciphered_text = ""

    print("text: ", text)
    print("key: ", key)
    print("Alfabet length: ", ALPHABET_LENGTH)

    ciphered_val = 0
    ciphered_text = ""

    for i in range(length):
        if(text[i].isupper()):
            ciphered_val = ((ord(text[i]) - START_VAL_UPPER) + key) % ALPHABET_LENGTH
            ciphered_char = chr(START_VAL_UPPER + ciphered_val)
            # print("Ciphered Val: ", ciphered_val)
            # print("Ciphered Char: ", ciphered_char)

        else:
            ciphered_val = ((ord(text[i]) - START_VAL_LOWER) + key) % ALPHABET_LENGTH
            ciphered_char = chr(START_VAL_LOWER + ciphered_val)
            # print("Ciphered Val: ", ciphered_val)
            # print("Ciphered Char: ", ciphered_char)
        
        ciphered_text += ciphered_char

    return ciphered_text

def caesar_decryption(text):
    length = len(text)
    ciphered_val = 0
    original_char = ""

    for key in range(1, ALPHABET_LENGTH+1):
        print("Key: ", key)
        original_text = ""
        for i in range(length):
            if(text[i].isupper()):
                ciphered_val = ((ord(text[i]) - START_VAL_UPPER) - key) % ALPHABET_LENGTH
                original_char = chr(START_VAL_UPPER + ciphered_val)

            else:
                ciphered_val = ((ord(text[i]) - START_VAL_LOWER) - key) % ALPHABET_LENGTH
                original_char = chr(START_VAL_LOWER + ciphered_val)
                # print("Ciphered Val: ", ciphered_val)
                # print("Ciphered Char: ", ciphered_char)

            original_text += original_char
        
        print(original_text)
        

if __name__ == "__main__":
    main()