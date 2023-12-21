
def filter_chars(string):
    new_string = ""
    for i, char in enumerate(string):
        if i >= 221 and i < 419:
            if char > "-" and char < "v":
                new_string += char
        else:
            new_string += char
    return new_string
