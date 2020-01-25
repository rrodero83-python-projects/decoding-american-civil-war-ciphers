"""Encrypt a path through a Union Route Cipher.

Designed for whole­word transposition ciphers with variable rows & columns.
Assumes encryption began at either top or bottom of a column.
Key indicates the order to read columns and the direction to traverse.
Negative column numbers mean start at bottom and read up.
Positive column numbers mean start at top & read down.

Example below is for 4x4 matrix with key ­1 2 ­3 4.
Note "0" is not allowed.
Arrows show encryption route; for negative key values read UP.

  1   2   3   4
 ___ ___ ___ ___
| ^ | | | ^ | | | MESSAGE IS WRITTEN
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | ACROSS EACH ROW
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | IN THIS MANNER
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | LAST ROW IS FILLED WITH DUMMY WORDS
|_|_|_v_|_|_|_v_|
START        END

Required inputs - a text message

Prints encrypted plaintext
"""
import random
import load_dictionary

# ==============================================================================
# USER INPUT:

#  the string to be encrypted (type or paste between triple­quotes):
plaintext = """We will run the batteries at Vicksburg the night of April 16 and proceed to Grand Gulf where 
we will reduce the forts. Be prepared to cross the river on April 25 or 29. Admiral Porter."""

# END OF USER INPUT - DO NOT EDIT BELOW THIS LINE!
# ==============================================================================

CODE_WORDS = {'BATTERIES': 'HOUNDS', 'VICKSBURG': 'ODOR', 'APRIL': 'CLAYTON', '16': 'SWEET', 'GRAND': 'TREE',
              'GULF': 'OWL', 'FORTS': 'BAILEY', 'RIVER': 'HICKORY', '25': 'MULTIPLY', '29': 'ADD', 'ADMIRAL': 'HERMES',
              'PORTER': 'LANGFORD'}

COLS = 6
ROWS = 7

KEY = [-1, 3, -2, 6, 5, -4]


def main():
    """Run program and print encrypted ciphertext."""
    print("\nPlaintext = {}".format(plaintext))

    textlist = list(plaintext.replace('.', '').split())
    textlist = replace_code_words(textlist)
    fill_dummy_words(textlist)
    translation_matrix = build_matrix(textlist)
    ciphertext = encrypt(translation_matrix)

    print("\nCiphertext = {}".format(ciphertext))


def replace_code_words(plaintext_list):
    return [CODE_WORDS.get(word.upper()) if word.upper() in CODE_WORDS.keys() else word.upper() for word in
            plaintext_list]


def fill_dummy_words(textlist):
    """Fills the bottom row with random dummy words"""
    len_cipher = len(textlist)
    dict_list = load_dictionary.load("dict.txt")
    compare = ROWS * COLS
    if compare != len_cipher and compare > len_cipher:
        for i in range(compare - len_cipher):
            textlist.append(random.choice(dict_list).upper())



def build_matrix(textlist):
    translation_matrix = []
    for i in range(ROWS):
        matrix_row = []
        for j in range(COLS):
            matrix_row.append(textlist[i * COLS + j])
        translation_matrix.append(matrix_row)
    return translation_matrix


def encrypt(translation_matrix):
    ciphertext = ''
    for k in KEY:
        for i in range(ROWS):
            if k > 0:
                ciphertext += translation_matrix[i][abs(k) - 1] + ' '
            elif k < 0:
                ciphertext += translation_matrix[-(i + 1)][abs(k) - 1] + ' '
    return ciphertext


if __name__ == '__main__':
    main()
