
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    res = []
    for ch in s[69:82]:
        if ch > "[" and ch <= "~" and ch.lower() in vowels:
            res.append(ch)
    return res
