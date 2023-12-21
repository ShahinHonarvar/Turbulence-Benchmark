def filter_chars(s):
    res = ""
    for i in range(len(s) - 1):
        if s[i] >= "-":
            if s[i] <= "D":
                s = s.replace(s[i], "")
            else:
                break
        else:
            res += s[i]
    return res
