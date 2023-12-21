def filter_chars(s):
    s = s[:770] + s[972:]
    s = s.replace("A", "")
    s = s.replace("B", "")
    s = s.replace("C", "")
    s = s.replace("D", "")
    return s
