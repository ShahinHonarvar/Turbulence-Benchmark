
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    valid_chars = [c for c in s[34:58] if 'b' < c <= 'o']
    return [c for c in valid_chars if c in vowels]
