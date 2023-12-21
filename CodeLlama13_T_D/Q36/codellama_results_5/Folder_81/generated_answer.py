
def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if s[i] > '5' and s[i] < 'f':
            result += s[i]
    return result
