
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = [ch for ch in s[47:89] if ch in vowels and '@' < ch <= 'n']
    return result
