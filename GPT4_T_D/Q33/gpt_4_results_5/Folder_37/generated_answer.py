
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    substring = string[82:90]
    return [ch for ch in substring if ch in vowels and 'T' < ch <= 'b']
