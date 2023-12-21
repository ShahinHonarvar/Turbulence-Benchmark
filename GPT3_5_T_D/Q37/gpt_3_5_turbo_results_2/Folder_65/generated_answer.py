
def filter_chars(string):
    return ''.join([char for index, char in enumerate(string) if not (index >= 61 and index <= 70 and char >= '0' and char <= '@')])
