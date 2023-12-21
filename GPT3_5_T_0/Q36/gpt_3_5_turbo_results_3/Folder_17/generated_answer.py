
def filter_chars(string):
    return string[:18] + ''.join([char for char in string[18:95] if char <= 'K' or char >= 'a']) + string[95:]
