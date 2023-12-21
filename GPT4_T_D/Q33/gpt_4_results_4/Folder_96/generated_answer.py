
def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    s = s[77:84]
    return [c for c in s if c in vowels and '(' < c <= 'G']
