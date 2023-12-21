
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    res = []
    for ch in s[641:872]:
        if ch in vowels and ch > '>' and ch <= 'q':
            res.append(ch)
    return res
