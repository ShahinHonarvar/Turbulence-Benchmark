
def filter_chars(string):
    new_str = ""
    for i in range(221, 419):
        if string[i] > "-" and string[i] < "v":
            new_str += string[i]
    return new_str
