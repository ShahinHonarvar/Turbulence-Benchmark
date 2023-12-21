
def filter_chars(s):
    result = ''
    for i, c in enumerate(s):
        if 299 <= i < 418 and '9' < c < 'P':
            result += c
        else:
            result += s[i]
    return result
