
def filter_chars(string):
    return string[:18] + ''.join(char for char in string[18:82] if not ('W' <= char <= '[')) + string[82:]
