
def filter_chars(string):
    affected_chars = set(char for char in string[83:100] if '*' <= char <= 'j')
    return ''.join(char for char in string if char not in affected_chars)
