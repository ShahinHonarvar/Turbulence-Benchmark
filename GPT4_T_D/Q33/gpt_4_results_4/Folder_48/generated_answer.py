
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = [ch for ch in s[529:828] if ch in vowels and 'U' < ch <= 'l']
    return result
