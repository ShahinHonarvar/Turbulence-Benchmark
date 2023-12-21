
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    _s = s[43:70]
    return [c for c in _s if c in vowels and 'b' >= c > '*']
