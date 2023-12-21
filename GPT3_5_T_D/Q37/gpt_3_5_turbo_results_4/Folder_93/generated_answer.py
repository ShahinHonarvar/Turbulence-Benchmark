
def filter_chars(string):
    return ''.join(char for i, char in enumerate(string) if (i < 38 or i > 69) or not ('H' <= char <= 'e'))
