
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    filtered_vowels = [ch for ch in s[23:85] if ch in vowels and 'W' < ch <= 'v']
    return filtered_vowels
