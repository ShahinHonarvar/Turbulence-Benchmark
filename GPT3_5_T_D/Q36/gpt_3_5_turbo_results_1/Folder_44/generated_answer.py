
def filter_chars(string):
    return string[:18] + ''.join(c for c in string[18:64] if not('3' < c < 'B')) + string[64:]
