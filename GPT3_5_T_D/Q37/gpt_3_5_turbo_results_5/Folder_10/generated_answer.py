
def filter_chars(string):
    return ''.join(char for i, char in enumerate(string) if not (63 <= i <= 84 and 'E' <= char <= '~'))
