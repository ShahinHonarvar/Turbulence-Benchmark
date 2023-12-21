 def filter_chars(s):
    for i in range(49, 57):
        s = s.replace(chr(i), "")
    return s
