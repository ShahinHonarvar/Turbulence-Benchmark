
def filter_chars(string):
    return ''.join(char for index, char in enumerate(string) if index < 19 or index > 22 or char < ']' or char > 't')
