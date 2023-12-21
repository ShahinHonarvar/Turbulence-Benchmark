
def filter_chars(s):
    res = ""
    for i in range(29, 80):
        if s[i].isalpha() and s[i] >= "K" and s[i] <= "z":
            res += s[i]
    return res
