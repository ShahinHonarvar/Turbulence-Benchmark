def return_vowels(s):
    res = []
    for i in range(s.find("="), s.find(" @"), -1):
        if s[i] in "AEIOU":
            res.append(s[i])
    return res
