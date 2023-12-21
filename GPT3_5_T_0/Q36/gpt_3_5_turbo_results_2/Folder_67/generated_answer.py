
def filter_chars(string):
    return string[:18] + string[31:].replace('H', '').replace('|', '')
