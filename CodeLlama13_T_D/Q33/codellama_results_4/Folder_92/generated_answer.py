
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [c for c in s[3:8] if c in vowels and c <= 'D' and c > ';']
