
def filter_chars(string):
    return string[:78] + string[81:].replace(string[78:81], "")
