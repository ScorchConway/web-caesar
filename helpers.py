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
    #print('alpha index of a:', alphabet_position('a'))
    #print('alpha index of A:', alphabet_position('A'))
    #print('alpha index of j:', alphabet_position('j'))
    for i in range(26):
        print('rotate_character', rotate_character('M', i))
    #print('A plus 1 place:', rotate_character('A', 1))

    #print('z plus 10 place:', rotate_character('z', 10))
if __name__ == '__main__':
        main()