def return_vowels(s):
    vow = range(37, 57)
    res = [c for c in s if c in vow and c not in " *P"]
    return res
