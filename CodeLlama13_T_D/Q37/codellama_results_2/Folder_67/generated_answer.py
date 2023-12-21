
def filter_chars(string):
    new_str = ""
    for i, c in enumerate(string):
        if i < 19 or i > 22 or c not in "]t":
            new_str += c
    return new_str
