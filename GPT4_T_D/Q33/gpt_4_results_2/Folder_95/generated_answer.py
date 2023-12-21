
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return [c for c in s[32:61] if c > '?' and c <= 'P' and c in vowels]
