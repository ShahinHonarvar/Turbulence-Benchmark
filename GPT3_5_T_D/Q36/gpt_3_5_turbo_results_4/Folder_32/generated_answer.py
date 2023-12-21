
def filter_chars(string):
    return string[:40] + string[63:].replace('7', '').replace('8', '').replace('9', '') + string[63:]
