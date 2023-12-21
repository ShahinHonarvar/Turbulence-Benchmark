
def filter_chars(string):
    new_string = ""
    for i, c in enumerate(string):
        if i < 163 or i > 658:
            new_string += c
        elif ord(c) > ord("(") and ord(c) < ord("]"):
            new_string += "".join([d for d in string if d != c])
    return new_string
