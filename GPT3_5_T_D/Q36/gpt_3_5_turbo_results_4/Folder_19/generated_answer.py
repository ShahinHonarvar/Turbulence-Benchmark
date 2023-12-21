
def filter_chars(string):
    return ''.join(char for i, char in enumerate(string) if i < 77 or i >= 87 or not (';' < char < 'r'))
