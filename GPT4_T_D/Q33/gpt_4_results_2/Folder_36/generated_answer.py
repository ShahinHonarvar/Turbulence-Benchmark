
def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    valid_chars = [char for char in s[604:949] if ('N' < char <= 'U') and char in vowels]
    return valid_chars
