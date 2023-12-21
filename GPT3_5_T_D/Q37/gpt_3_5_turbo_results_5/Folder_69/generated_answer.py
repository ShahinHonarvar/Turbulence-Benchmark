
def filter_chars(string):
    return ''.join([char for index, char in enumerate(string) if not (114 <= index <= 639 and '!' <= char <= 'x')])
