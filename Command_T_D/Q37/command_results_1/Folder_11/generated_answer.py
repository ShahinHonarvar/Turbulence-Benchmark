def filter_chars(s):
    s=s[29:97]
    s=s[s.index("-"):s.index("n")]
    s=s.replace(" ","")
    return s
