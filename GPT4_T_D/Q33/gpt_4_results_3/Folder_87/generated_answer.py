
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [c for c in s[34:58].lower() if c > 'b' and c <= 'o' and c in vowels]
