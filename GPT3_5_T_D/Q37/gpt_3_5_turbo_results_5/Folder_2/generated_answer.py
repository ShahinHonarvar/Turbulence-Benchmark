
def filter_chars(string):
    return "".join([char for i, char in enumerate(string) if i < 477 or i > 984 or char < ',' or char > 'V'])
