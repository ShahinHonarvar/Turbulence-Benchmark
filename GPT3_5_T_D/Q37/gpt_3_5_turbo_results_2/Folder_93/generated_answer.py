
def filter_chars(string):
    return "".join([char for char in string if char not in string[38:70] or char < 'H' or char > 'e'])
