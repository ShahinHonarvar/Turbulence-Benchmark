
def filter_chars(string):
    new_string = ""
    for i, char in enumerate(string):
        if i < 343 or i > 665:
            new_string += char
        elif char >= "%" and char <= "U":
            new_string += char
        else:
            new_string += "".join([c for c in string if c != char])
    return new_string
