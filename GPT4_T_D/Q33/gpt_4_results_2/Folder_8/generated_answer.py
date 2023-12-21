
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    res = []
    for char in s[64:82]:
        if char in vowels and 'P' < char <= 'z':
            res.append(char)
    return res
