def filter_chars(s):
    s = s[0:10] + s[11:-69] + s[-1:]
    return s.replace("I", "")
