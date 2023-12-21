
def filter_chars(s):
    start = 35
    end = 98
    new_str = ""
    for i in range(start, end + 1):
        if s[i].isalpha() and s[i].lower() >= 'a' and s[i].lower() <= 'b':
            continue
        else:
            new_str += s[i]
    return new_str
