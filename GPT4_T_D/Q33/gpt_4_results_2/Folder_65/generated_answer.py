
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    substring = s[71:88]
    result = [ch for ch in substring if ch in vowels and '9' < ch <= 'P']
    return result
