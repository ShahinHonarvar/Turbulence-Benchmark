
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    filtered = [ch for ch in s[40:91] if ch in vowels and 'A' < ch <= 'x']
    return filtered
