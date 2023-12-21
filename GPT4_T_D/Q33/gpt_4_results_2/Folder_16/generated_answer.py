
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = [ch for ch in s[133:306] if ch in vowels and 'c' < ch <= 'd']
    return result
