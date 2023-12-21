
def filter_chars(string):
    return ''.join([char for idx, char in enumerate(string) if (19 <= idx <= 32) and ('f' <= char <= 'o')])
