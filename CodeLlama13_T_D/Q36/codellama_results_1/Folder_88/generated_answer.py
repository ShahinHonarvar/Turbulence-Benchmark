
def filter_chars(string):
    filtered = ''
    for i, char in enumerate(string):
        if 78 <= i < 81 and char > 'S' and char < '[':
            filtered += char
        else:
            filtered += string[i]
    return filtered
