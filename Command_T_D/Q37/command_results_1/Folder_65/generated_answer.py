def filter_chars(s):
    i = s.find("`")
    j = s.find("`", i + 1)
    for c in range(ord("0"), ord("@") + 1):
        if s[i:j + 1].count(chr(c)) > 0:
            s = s.replace(chr(c), "")
    return s
