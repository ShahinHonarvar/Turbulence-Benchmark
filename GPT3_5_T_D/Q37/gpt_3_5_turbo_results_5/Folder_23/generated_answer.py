
def filter_chars(string):
    return ''.join(char for i, char in enumerate(string) if i < 51 or i > 77 or not('V' <= char <= 'Y'))
