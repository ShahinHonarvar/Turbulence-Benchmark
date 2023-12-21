
def filter_chars(string):
    return string[:18] + string[38:].replace(')', '').replace('(', '') + string[18:38]
