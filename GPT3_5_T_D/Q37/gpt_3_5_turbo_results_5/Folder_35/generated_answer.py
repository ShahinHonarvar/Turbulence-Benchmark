
def filter_chars(string):
    return ''.join(char for i, char in enumerate(string) if not (155 <= i <= 403 and '(' <= char <= ']'))
