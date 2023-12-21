
def filter_chars(s):
    result = ''
    for i, c in enumerate(s):
        if i < 323 or i > 526:
            result += c
        elif c < ')':
            result += c
        else:
            result += 'O'
    return result
