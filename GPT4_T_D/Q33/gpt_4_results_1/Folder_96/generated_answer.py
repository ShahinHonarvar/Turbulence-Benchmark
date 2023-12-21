
def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    sub = s[77:84]
    return [c for c in sub if c in vowels and c > '(' and c <= 'G']
