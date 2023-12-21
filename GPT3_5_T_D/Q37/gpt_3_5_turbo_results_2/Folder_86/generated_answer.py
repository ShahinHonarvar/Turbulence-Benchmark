
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if not (164 <= i <= 706 and 'O' <= char <= '}')])
