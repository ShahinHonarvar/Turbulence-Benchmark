def return_vowels(s):
    i = s.find("@") + 1
    j = s.find("n")
    if i == j:
        return []
    else:
        return s[i:j]
