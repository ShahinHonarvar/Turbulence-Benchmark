
def filter_chars(string):
    return ''.join([char for idx, char in enumerate(string) if not (33 <= idx <= 70 and '7' <= char <= 'k')])
