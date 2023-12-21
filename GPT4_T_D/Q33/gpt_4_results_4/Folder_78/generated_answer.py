
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    char_list = [c for c in string[46:90] if ('@' < c <= '[') and (c in vowels)]
    return char_list
