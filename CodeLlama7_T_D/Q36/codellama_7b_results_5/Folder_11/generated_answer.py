 def filter_chars(s):
    for i in range(86, 93):
        s = s.replace(chr(i), "")
    return s
