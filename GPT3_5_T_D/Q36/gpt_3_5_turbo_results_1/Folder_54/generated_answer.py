
def filter_chars(string):
    return string[:18] + ''.join([char for char in string[18:38] if ')' < char < 'P']) + string[38:]
