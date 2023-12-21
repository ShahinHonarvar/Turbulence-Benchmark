
def filter_chars(string):
    return ''.join(char for index, char in enumerate(string) if index < 57 or index > 96 or not ('<' <= char <= 'w'))
