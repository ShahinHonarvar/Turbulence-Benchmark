
def filter_chars(s):
    result = ""
    for i, c in enumerate(s):
        if i >= 10 and i <= 52 and ord(c) >= ord('@') and ord(c) <= ord('T'):
            result += c
        else:
            result += s[i]
    return result
