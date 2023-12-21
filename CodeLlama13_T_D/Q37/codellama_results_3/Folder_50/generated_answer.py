
def filter_chars(s):
    result = ''
    for i, c in enumerate(s):
        if i < 71 or i > 96:
            result += c
        elif c >= '_' and c <= 'o':
            result += c
    return result
