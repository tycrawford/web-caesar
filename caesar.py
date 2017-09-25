from helpers import alphabet_position, rotate_character
import string
def rotate_string(strinput, rot_by):
    rot_by = int(rot_by)
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
  
from helpers import alphabet_position, rotate_character

def encrypt(strinput, rot_by):
    newstring = ""
    rot_by = int(rot_by)
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
        new_char = str(new_char)
        newstring = newstring + new_char
    return newstring

def main():
    starter_message = input("Type a message:")
    starter_rotation = input("Rotate by:")
    print(encrypt(starter_message, starter_rotation))

if __name__ == "__main__":
    main()
    