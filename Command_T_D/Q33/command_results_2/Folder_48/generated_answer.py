def return_vowels(s):
    v = list(s[529:828])
    if v.count("U") > 1:
        v.remove("U")
    if v.count("L") > 1:
        v.remove("L")
    return v
