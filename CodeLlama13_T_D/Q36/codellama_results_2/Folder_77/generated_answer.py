
def filter_chars(string):
    new_string = ""
    for i, c in enumerate(string):
        if i < 221 or i > 419 or ord(c) <= ord("-") or ord(c) >= ord("v"):
            new_string += c
    return new_string
