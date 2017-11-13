from helpers import alphabet_position, rotate_character

def rotate_string(text, rot):
    """encrypts the text with an int rotation that advances each character by rot places
    """
    
    if(rot < 0):
        rot = 26 + rot # equivalent to 26 - abs(rot)
    result = ''
    for char in text:
        if 97 <= ord(char) <= 122: # char is lowercase
            ascii_value_after_rot = (ord(char) - 97 + rot) % 26 + 97
            # print('post rot:', ascii_value_after_rot)
            result += chr(ascii_value_after_rot)
        elif 65 <= ord(char) <= 90: #char is uppercase
            ascii_value_after_rot = (ord(char) - 65 + rot) % 26 + 65
            # print('post rot:', ascii_value_after_rot)
            result += chr(ascii_value_after_rot)

        else:
            result += char
    #print("the result is:", result)
    return result

def rot13(mess):
    return rotate_string(mess, 13)

def alphabet_position(char):
    """accepts an alphabetic character, and
    returns a zero-based index of that character in the alphabet."""

    if not str.isalpha(char):
        return 0
    if str.isupper(char):
        return ord(char) - ord('A')
    else:
        return ord(char) - ord('a')

def rotate_character(char, rot):
    """takes a string with a len-1 string, and a positive int.
    If char is an alphabetic char,
    returns a single char advanced by rot places,
    else returns the input char.
    """
    if str.isupper(char):
        return chr((ord(char) - ord('A') + rot) % 26 + ord('A'))

    elif str.islower(char):
        return chr((ord(char) - ord('a') + rot) % 26 + ord('a'))
    else:
        return char

def main():
    # print(rot13('abcde'))
    # print(rot13('nopqr'))
    # print(rot13(rot13('since rot thirteen is symmetric you should see this message')))
    # print(rot13(rot13('Since rot Thirteen Is Symmetric You should see this message')))
    print(rotate_string(input('Type a message:'), int(input('Rotate by:'))))

if __name__ == "__main__":
    main()