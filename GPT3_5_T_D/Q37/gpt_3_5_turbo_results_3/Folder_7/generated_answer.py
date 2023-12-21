
def filter_chars(string):
    return ''.join(char for index, char in enumerate(string) if index < 521 or index > 722 or not ('>' <= char <= '_'))
