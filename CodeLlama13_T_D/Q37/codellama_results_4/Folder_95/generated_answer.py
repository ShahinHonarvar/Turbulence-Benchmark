
def filter_chars(s):
    result = ''
    for i, c in enumerate(s):
        if not (35 <= i <= 40 and ord(')') <= ord(c) <= ord('l')):
            result += c
    return result
