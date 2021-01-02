import pprint

ALPHABET_LOWER = "abcdefghiklmnopqrstuvwxyz"
ALPHABET_UPPER = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
ALPHABET_LENGTH = 26
START_VAL_LOWER = 97
START_VAL_UPPER = 65

MATRIX_HEIGHT = 5 
MATRIX_WIDTH = 5 

pp = pprint.PrettyPrinter(indent=2)

def main():
    playfair_keyword = "MONARCHY"
    matrix = create_matrix(playfair_keyword, ALPHABET_UPPER)

    print("\n--------PLAYFAIR MATRIX-----------\n")
    pp.pprint(matrix)
    print("------------------------------------")

    text = "ATTACKATDAWN"
    text_digrams = digram_separation(text)
    print("Digrams: ", text_digrams)

    digram_shift = []
    for digram in text_digrams:
        # print("Digram: ", digram)

        d1_coor = letter_coor_in_matrix(digram[0], matrix)
        d2_coor = letter_coor_in_matrix(digram[1], matrix)

        # print("D1 Coor: ", d1_coor)
        # print("D2 Coor: ", d2_coor)

        # letter shift
        if(d1_coor[0] == d2_coor[0]): # row shift
            shift1 = matrix[d1_coor[0]][(d1_coor[1] + 1) % MATRIX_WIDTH]
            shift2 = matrix[d2_coor[0]][(d2_coor[1] + 1) % MATRIX_WIDTH]

            # print("Shift1: ", shift1)
            # print("Shift2: ", shift2) 
            digram_shift.append([shift1, shift2])
        elif(d1_coor[1] == d2_coor[1]): # column shift
            shift1 = matrix[(d1_coor[0] + 1) % MATRIX_HEIGHT][d1_coor[1]]
            shift2 = matrix[(d2_coor[0] + 1) % MATRIX_HEIGHT][d2_coor[1]]

            digram_shift.append([shift1, shift2])
        else: # digram shift
            shift1 = matrix[d1_coor[0]][d2_coor[1]]
            shift2 = matrix[d2_coor[0]][d1_coor[1]]
            digram_shift.append([shift1, shift2])

    encrypted_text = ""

    for digram in digram_shift:
        encrypted_text += "".join(digram)

    print("Encrypted text: ", encrypted_text)

def letter_coor_in_matrix(letter, matrix):
    x_coor = 0
    y_coor = 0
    
    for i in range(MATRIX_HEIGHT):
        for j in range(MATRIX_WIDTH):
            if(letter == matrix[i][j]):
                x_coor = i
                y_coor = j

    return (x_coor, y_coor)

def digram_separation(text):
    mod_text = text

    if(len(text) % 2 != 0):
        mod_text += "X"

    step = 2
    length = len(mod_text)
    text_array = str_to_array(mod_text)

    # if text contains J it replaces it with an I
    for i in range(len(text_array)):
        if(text_array[i] == "J"):
            text_array[i] = "I"

    mod_text_array = []

    for i in range(0, length, step):
        if(text_array[i] == text_array[i+1]):
            text_array.insert(i+1, "X")
        
        mod_text_array.append(text_array[i:i+step])

    
    return mod_text_array



def create_matrix(text, alphabet):
    text_array = str_to_array(text)
    print("TEXT ARRAY: ", text_array)

    # if text contains J it replaces it with an I
    for i in range(len(text_array)):
        if(text_array[i] == "J"):
            text_array[i] = "I"

    text_set = list(dict.fromkeys(text_array))
    # print("TEXT SET: ", text_set)
    alphabet_array = str_to_array(alphabet)
    playfair_matrix = []

    for i in range(MATRIX_HEIGHT):
        matrix_row = []
        for j in range(MATRIX_WIDTH):
            if text_set:
                letter = text_set.pop(0)
                matrix_row.append(letter)
                letter_index = get_letter_index(letter, alphabet_array)
                # print("letter", letter, "letter_index", letter_index)
                alphabet_array.pop(letter_index)
            else:
                matrix_row.append(alphabet_array.pop(0))

        playfair_matrix.append(matrix_row)
    
    return playfair_matrix



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