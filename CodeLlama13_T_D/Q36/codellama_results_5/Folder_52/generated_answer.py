
def filter_chars(s):
    result = []
    for i, c in enumerate(s):
        if i < 49 or i > 56:
            result.append(c)
        elif ord(c) > ord('I') and ord(c) < ord('a'):
            for j, d in enumerate(result):
                if c == d:
                    del result[j]
                    break
    return ''.join(result)
