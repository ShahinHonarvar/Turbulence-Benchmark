
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    s_range = s[56:68]
    return [c for c in s_range if c in vowels and 'M' < c <= 'X']
