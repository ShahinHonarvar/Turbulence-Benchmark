
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    s = s[1:5]
    return [ch for ch in s if ch in vowels and ch > '!' and ch <= 'j']
