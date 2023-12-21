
def filter_chars(string):
    return string[:1] + string[1:9].replace('9', '').replace('a', '') + string[9:]
