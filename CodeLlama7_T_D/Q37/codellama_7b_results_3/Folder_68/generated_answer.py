
def filter_chars(s):
    start = 7
    end = 9

    for c in s[start:end+1]:
        if ord(c) < 6 or ord(c) > 119:
            s = s.replace(c, '')

    return s
