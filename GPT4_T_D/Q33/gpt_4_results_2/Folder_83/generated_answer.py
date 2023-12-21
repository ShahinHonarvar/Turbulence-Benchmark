
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    character_range = s[90:97]
    result = [ch for ch in character_range if ch in vowels and '_' < ch <= 'x']
    return result
