
def filter_chars(s):
    return ''.join([c for c in s if 29 <= ord(c) <= 97 and '-' <= c <= 'n'])
