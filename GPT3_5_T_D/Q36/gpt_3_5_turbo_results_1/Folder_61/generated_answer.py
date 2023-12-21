
def filter_chars(string):
    return ''.join(char for i, char in enumerate(string) if i < 3 or i >= 9 or not ('*' < char < 'E'))
