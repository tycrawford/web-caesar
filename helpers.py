def alphabet_position(letter):
    if letter.isupper():
        start_char = ord(letter) - 65
        return start_char
    elif letter.islower():
        start_char = ord(letter) - 97
        return start_char
    else:
        return "Not upper or lower"

def rotate_character(strinput,rot_by):
    newstring = ""
    for letter in strinput:
        start_char = 0
        if letter.isalpha(): 
            if letter.isupper():
                start_char = ord(letter) - 65
                new_char = chr(((start_char + rot_by) % 26) + 65)
            elif letter.islower():
                start_char = ord(letter) - 97
                new_char = chr(((start_char + rot_by) % 26) + 97)
        else:
            new_char = letter
        newstring = newstring + new_char
    return newstring  