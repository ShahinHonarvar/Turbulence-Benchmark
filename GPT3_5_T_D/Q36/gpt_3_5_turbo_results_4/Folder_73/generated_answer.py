
def filter_chars(string):
    return string[:66] + string[66:90].replace("#", "").replace("T", "") + string[90:]
