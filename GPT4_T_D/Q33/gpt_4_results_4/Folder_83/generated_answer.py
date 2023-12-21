
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    chars = list(s[90:97])
    return [ch for ch in chars if ch in vowels and '_' < ch <= 'x']
