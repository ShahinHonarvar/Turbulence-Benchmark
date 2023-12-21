
def filter_chars(string):
    return string[:35] + ''.join(c for c in string[35:99] if not ('A' <= c <= 'b')) + string[99:]
