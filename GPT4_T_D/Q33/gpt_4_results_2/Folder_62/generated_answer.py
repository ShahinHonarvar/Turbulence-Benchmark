
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return [ch for ch in s[14:60] if ch in vowels and 'D' < ch <= 'v']
