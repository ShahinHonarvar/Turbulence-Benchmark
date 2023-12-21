
def filter_chars(string):
    new_string = ""
    for i, char in enumerate(string):
        if i < 318 or i > 337:
            new_string += char
    return new_string
