
def filter_chars(s):
    result = ''
    for i in range(1, 7):
        if s[i] > '3' and s[i] < '^':
            result += s[:i] + s[i+1:]
        else:
            result += s[i]
    return result
