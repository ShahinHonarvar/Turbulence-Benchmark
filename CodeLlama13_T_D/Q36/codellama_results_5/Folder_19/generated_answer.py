
def filter_chars(s):
    result = ''
    for i, char in enumerate(s):
        if 77 <= ord(char) < 87 and s[i] > ';' and s[i] < 'r':
            result += char
    return result
