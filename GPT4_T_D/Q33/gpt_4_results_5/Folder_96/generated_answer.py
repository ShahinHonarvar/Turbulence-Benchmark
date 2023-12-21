
def return_vowels(string):
    sublist = string[77:84]
    vowel_list = ['A', 'E', 'I', 'O', 'U']
    filtered_vowels = [c for c in sublist if c in vowel_list and '(' < c <= 'G']
    return filtered_vowels
