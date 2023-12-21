def filter_chars(string):
    string = string[:3] + string[6:]
    string = string.replace("g", "")
    return string
