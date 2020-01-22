r"""Encrypt a Civil War 'rail fence' type cipher.

This is for a "3­rail" fence cipher for short messages.

Example text to encrypt: 'We are discovered flee at once'

Rail fence style:  W   E   C   R   L   T   E
                    E R D S O E E F E A O C
                     A   I   V   D   E   N

Read zigzag:       \/\/\/\/\/\/\/\/\/\/

Encrypted:  WECRL TEERD SOEEF EAOC AIVD EN

"""

# ------------------------------------------------------------------------------
# USER INPUT:

# the string to be encrypted (paste between quotes):
plaintext = """Let us cross over the river and rest under the shade of the trees
"""

# END OF USER INPUT - DO NOT EDIT BELOW THIS LINE!
# ------------------------------------------------------------------------------

def main():
    """Run program to encrypt message using 3­rail rail fence cipher."""
    message = prep_plaintext(plaintext)
    rails = build_rails(message)
    encrypt(rails)


def prep_plaintext(plaintext):
    """Remove spaces & leading/trailing whitespace."""
    message = "".join(plaintext.split())
    message = message.upper()  #  convention for ciphertext is uppercase
    print("\nplaintext = {}".format(plaintext))
    return message


def build_rails(message):
    """Build strings with every other letter in a message."""
    rail_1 = message[::4]
    rail_2 = message[1::2]
    rail_3 = message[2::4]
    rails = rail_1 + rail_2 + rail_3
    return rails


def encrypt(rails):
    """Split letters in ciphertext into chunks of 5 & join to make string."""
    ciphertext = ' '.join([rails[i:i + 5] for i in range(0, len(rails), 5)])
    print("ciphertext = {}".format(ciphertext))


if __name__ == '__main__':
    main()
