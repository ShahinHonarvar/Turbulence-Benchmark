
def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if s[i] > 't' and s[i] < 'v':
            continue
        result += s[i]
    return result
