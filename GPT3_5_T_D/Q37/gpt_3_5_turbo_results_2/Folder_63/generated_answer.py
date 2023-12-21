
def filter_chars(string):
    return ''.join(char for i, char in enumerate(string) if not (42 <= i <= 92 and '/' <= char <= 'a'))
