
def return_vowels(s):
    english_vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vowels_in_range = [c for c in s[40:91] if c in english_vowels and 'A' < c <= 'x']
    return vowels_in_range
