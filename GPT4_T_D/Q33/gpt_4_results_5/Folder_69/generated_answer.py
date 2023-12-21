
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    string_subset = string[641:872]
    char_list = [char for char in string_subset if char > '>' and char <= 'q' and char in vowels]
    return char_list
