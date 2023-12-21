
def filter_chars(string):
    return ''.join(char for index, char in enumerate(string) if index < 503 or index > 753 or not ('9' <= char <= 'w'))
