r"""Decrypt a Civil War 'rail fence' type cipher.

This is for a "3­rail" fence cipher for short messages.

Example text to encrypt: 'We are discovered flee at once'

Rail fence style:  W   E   C   R   L   T   E
                    E R D S O E E F E A O C
                     A   I   V   D   E   N

Read zigzag:       \/\/\/\/\/\/\/\/\/\/

Encrypted:  WECRL TEERD SOEEF EAOC AIVD EN

"""

import math
import itertools

# ------------------------------------------------------------------------------
# USER INPUT:

#  the string to be decrypted (paste between quotes):
ciphertext = """LSSEE EDTEE DTREU COSVR HRVRN RSUDR HSAEF HTEST ROTIA ENTHO EE
"""

# END OF USER INPUT - DO NOT EDIT BELOW THIS LINE!
# ------------------------------------------------------------------------------


def main():
    """Run program to decrypt message using 3­rail rail fence cipher."""
    message = prep_ciphertext(ciphertext)
    row1, row2, row3 = split_rails(message)
    decrypt(row1, row2, row3)


def prep_ciphertext(ciphertext):
    """Remove whitespace."""
    message = "".join(ciphertext.split())
    print("\nciphertext = {}".format(ciphertext))
    return message


def split_rails(message):
    """Split message in two, always rounding UP for 1st row."""
    row_1_len = math.ceil(len(message)/4)
    row_2_len = row_1_len * 2
    row1 = message[:row_1_len]
    row2 = message[row_1_len:row_1_len + row_2_len]
    row3 = message[row_1_len + row_2_len:]
    return row1, row2, row3


def decrypt(row1, row2, row3):
    """Build list with every other letter in 2 strings & print."""
    plaintext = []
    ciclo = 0
    for r1, r3 in itertools.zip_longest(row1, row3):
        plaintext.append(r1.lower())
        plaintext.append(row2[ciclo].lower())
        plaintext.append(r3.lower())
        ciclo += 1
        plaintext.append(row2[ciclo].lower())
        ciclo += 1

    if None in plaintext:
        plaintext.pop()

    print("rail 1 = {}".format(row1))
    print("rail 2 = {}".format(row2))
    print("rail 3 = {}".format(row3))
    print("\nplaintext = {}".format(''.join(plaintext)))


if __name__ == '__main__':
    main()
