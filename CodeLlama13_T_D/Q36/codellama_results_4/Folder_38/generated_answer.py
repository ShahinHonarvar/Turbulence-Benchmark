
def filter_chars(string):
    filtered = ''
    for i, char in enumerate(string):
        if i < 44 or i > 48:
            filtered += char
        elif string[i-1] == '+' and string[i+1] == 'l':
            continue
        else:
            filtered += char
    return filtered
