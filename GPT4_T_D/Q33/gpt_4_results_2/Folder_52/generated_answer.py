
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    res = [ch for ch in s[24:68] if ch in vowels and 'f' < ch <= '|']
    return res
