
def filter_chars(string):
    return string[:41] + string[56:].replace("Z", "").replace("a", "").replace("b", "") + string[56:]
