
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return [ch for ch in s[28:76] if ch > '+' and ch <= 'z' and ch in vowels]
