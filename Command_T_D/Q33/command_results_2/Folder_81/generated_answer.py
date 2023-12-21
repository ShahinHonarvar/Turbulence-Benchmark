def return_vowels(s):
    res = []
    for c in s[5:]:
        if c == "M":
            break
        elif c.isupper() and c.islower() and c in "AEIOU":
            res.append(c)
    return res
