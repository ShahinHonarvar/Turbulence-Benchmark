
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    chars = [c for c in s[20:43] if '5' < c <= 'M' and c in vowels]
    return chars
