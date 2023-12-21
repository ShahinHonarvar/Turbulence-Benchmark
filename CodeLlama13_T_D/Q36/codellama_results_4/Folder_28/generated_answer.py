
def filter_chars(string):
    result = []
    for i, c in enumerate(string):
        if i < 31 or i > 73:
            result.append(c)
        elif ord(c) > ord('M') and ord(c) < ord('j'):
            continue
        else:
            result.append(c)
    return ''.join(result)
