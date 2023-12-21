
def filter_chars(string):
    return ''.join(char for i, char in enumerate(string) if not (2 <= i <= 6 and '?' <= char <= 'f'))
