
def filter_chars(string):
    new_str = ""
    for i in range(42, 78):
        if string[i] > "!" and string[i] < "?":
            new_str += string[i]
    return new_str
