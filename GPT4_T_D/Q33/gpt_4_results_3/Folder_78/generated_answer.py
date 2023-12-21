
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [ch for ch in s[46:90] if ch in vowels and '@' < ch <= '[']
