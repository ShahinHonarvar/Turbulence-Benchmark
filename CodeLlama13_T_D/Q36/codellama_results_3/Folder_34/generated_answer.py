
def filter_chars(string):
    new_str = ""
    for i in range(10, 79):
        if string[i] > "?" and string[i] < "m":
            new_str += string[i]
    return new_str
