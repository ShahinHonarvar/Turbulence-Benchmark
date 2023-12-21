
def filter_chars(string):
    return ''.join(char for index, char in enumerate(string) if index < 12 or index > 77 or not (char >= ':' and char <= 'L'))
