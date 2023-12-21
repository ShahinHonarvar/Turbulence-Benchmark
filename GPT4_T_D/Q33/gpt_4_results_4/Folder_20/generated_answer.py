
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    subset = string[59:61]
    valid_chars = [char for char in subset if '+' < char <= 'h' and char in vowels]
    return valid_chars
