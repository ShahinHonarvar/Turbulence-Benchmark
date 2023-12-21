

def filter_chars(string):
    return string[:18] + ''.join(c for c in string[18:95] if not ('K' < c < 'a')) + string[95:]
