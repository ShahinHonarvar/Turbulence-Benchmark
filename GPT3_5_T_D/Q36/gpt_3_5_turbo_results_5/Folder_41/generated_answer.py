
def filter_chars(string):
    return string[:81] + string[81:89].replace('g', '').replace('h', '').replace('i', '').replace('j', '') + string[89:]
