
def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if s[i] >= '5' and s[i] <= '_':
            continue
        else:
            result += s[i]
    return result
