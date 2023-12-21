
def filter_chars(string):
    return ''.join([char for index, char in enumerate(string) if 57 <= index < 69 and '(' < char < 'W'])
