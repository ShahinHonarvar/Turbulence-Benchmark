
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = [c for c in s[2:7] if c in vowels and '^' < c <= 'd']
    return result
