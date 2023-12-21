
def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if s[i].isalpha() and 'S' <= s[i] <= '{':
            result += s[i]
    return result
