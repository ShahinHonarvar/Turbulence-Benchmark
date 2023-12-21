
def filter_chars(s):
    for char in s[324:526]:
        if char > ')' and char < 'O':
            s = s.replace(char, '')
    return s
