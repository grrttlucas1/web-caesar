def alphabet_position(letter):
    """For a given letter, return it's position in the alphabet."""
    letter   = letter.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for idx in range(len(alphabet)):
        if  letter == alphabet[idx]:
            letter_position = idx
    return letter_position


def rotate_character(char, rot):
    """Receives a character char and and integer rot.  Rotates char by rot
    number of places.
    """
    if not char.isalpha():
        return char

    char_pos_current = alphabet_position(char)
    alphabet         = "abcdefghijklmnopqrstuvwxyz"
    char_pos_new     = (char_pos_current + rot) % 26
    new_char         = alphabet[char_pos_new]

    if char.isupper():
        return new_char.upper()
    else:
        return new_char

def encrypt(text, rot):
    """Receives a string text and an integer rot.  Rotates text by rot
    number of places."""
    new_text = ""
    for character in text:
        new_text = new_text + rotate_character(character, rot)
    return new_text