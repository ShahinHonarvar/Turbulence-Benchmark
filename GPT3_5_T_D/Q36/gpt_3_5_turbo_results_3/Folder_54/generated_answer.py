
def filter_chars(string):
    return string[:18] + ''.join([c for c in string[18:38] if c <= ')' or c >= 'P']) + string[38:]
