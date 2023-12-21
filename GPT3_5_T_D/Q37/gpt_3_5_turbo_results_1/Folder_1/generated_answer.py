
def filter_chars(string):
    return ''.join(char for index, char in enumerate(string) if index < 41 or index > 79 or char < 'f' or char > '|')
