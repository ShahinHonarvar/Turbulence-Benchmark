
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    substring = s[70:76]
    return [c for c in substring if c in vowels and '2' < c <= ':']
