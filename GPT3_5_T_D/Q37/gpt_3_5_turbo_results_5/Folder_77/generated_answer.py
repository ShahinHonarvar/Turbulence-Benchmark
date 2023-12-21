
def filter_chars(string):
    return ''.join(char for i, char in enumerate(string) if i < 384 or i > 411 or not ('/' <= char <= '8'))
