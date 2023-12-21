
def return_vowels(s):
    subset = s[202:872]
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = [ch for ch in subset if ch in vowels and '3' < ch <= '>']
    return result
