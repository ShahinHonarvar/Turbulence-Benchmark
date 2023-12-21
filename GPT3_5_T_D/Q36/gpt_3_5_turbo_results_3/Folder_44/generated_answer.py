
def filter_chars(string):
    return string[:18] + string[18:64].replace('4', '').replace('5', '').replace('6', '').replace('7', '').replace('8', '').replace('9', '') + string[64:]
