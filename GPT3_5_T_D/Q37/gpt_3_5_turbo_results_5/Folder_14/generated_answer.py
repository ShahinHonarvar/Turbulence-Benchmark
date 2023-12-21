
def filter_chars(string):
    return ''.join(char for index, char in enumerate(string) if index < 35 or index > 98 or char < 'A' or char > 'b')
