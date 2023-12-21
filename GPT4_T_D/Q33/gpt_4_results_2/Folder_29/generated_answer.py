
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = [c for c in s[19:20] if c in vowels and 'p' >= c > '<']
    return result
