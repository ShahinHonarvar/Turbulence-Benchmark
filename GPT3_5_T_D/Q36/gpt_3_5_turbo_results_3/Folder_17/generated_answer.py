
def filter_chars(string):
    return string[:18] + ''.join([c for c in string[18:95] if c <= 'K' or c >= 'a']) + string[95:]
