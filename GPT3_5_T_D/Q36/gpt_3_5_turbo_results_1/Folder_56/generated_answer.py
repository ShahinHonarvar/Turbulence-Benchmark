
def filter_chars(string):
    filtered = []
    for char in string:
        if 31 < ord(char) < 50 and '/' < char < 'J':
            continue
        filtered.append(char)
    return ''.join(filtered)
