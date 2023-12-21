
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    letters = s[24:59]
    result = [c for c in letters if c in vowels and 'N' < c <= 'U']
    return result
