
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    res = [ch for ch in s[142:145] if ch in vowels and '4' < ch <= 'o']
    return res
