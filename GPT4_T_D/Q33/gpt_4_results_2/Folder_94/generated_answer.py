
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    res = []
    for ch in s[40:94]:
        if ch in vowels and '4' < ch <= 'H':
            res.append(ch)
    return res
