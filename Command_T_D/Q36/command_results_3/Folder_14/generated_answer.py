def filter_chars(s):
    i = s.find("Z")
    j = s.find("c")
    return s[:i] + s[i+1:j] + s[j+1:]
