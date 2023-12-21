
def filter_chars(s):
    for char in s[55:92]:
        if char > 'J' and char < 'X':
            s = s.replace(char, '')
    return s
