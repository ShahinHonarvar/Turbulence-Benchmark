
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = [c for c in s[5:6] if c in vowels and '3' < c <= '^']
    return result
