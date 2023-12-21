
def filter_chars(s):
    result = ""
    for i in range(10, 80):
        if s[i].isalpha() and s[i].lower() >= 'a' and s[i].lower() < 'm':
            result += s[i]
    return result
