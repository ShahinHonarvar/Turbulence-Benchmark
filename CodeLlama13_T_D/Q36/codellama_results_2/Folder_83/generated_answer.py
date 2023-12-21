
def filter_chars(string):
    return "".join([char for char in string if ord(char) not in range(72, 93) or char < '<' or char > 'J'])
