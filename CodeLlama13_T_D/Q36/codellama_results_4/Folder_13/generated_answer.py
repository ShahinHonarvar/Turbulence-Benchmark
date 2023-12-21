
def filter_chars(string):
    result = ''
    for i, char in enumerate(string):
        if 323 <= i < 526 and ')' < char < 'O':
            continue
        else:
            result += char
    return result
