
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = [ch for ch in s[10:82] if ch > '$' and ch <= '@' and ch in vowels]
    return result
