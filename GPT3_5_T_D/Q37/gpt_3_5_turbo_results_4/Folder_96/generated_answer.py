
def filter_chars(string):
    return string[:86] + string[92:].replace("!", "").replace("s", "") + string[92:]
