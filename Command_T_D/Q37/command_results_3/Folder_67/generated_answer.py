def filter_chars(s):
    i = s.find(']')
    j = s.find('t', i + 1)
    return s[:i] + s[i+1:j] + s[j+1:]
