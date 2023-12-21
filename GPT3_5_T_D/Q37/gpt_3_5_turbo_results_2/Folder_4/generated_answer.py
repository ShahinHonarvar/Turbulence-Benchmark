
def filter_chars(string):
    return "".join([char for index, char in enumerate(string) if index < 19 or index > 33 or char < 'S' or char > '{'])
