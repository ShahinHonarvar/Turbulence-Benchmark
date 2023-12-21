
def filter_chars(string):
    new_string = ""
    for i, char in enumerate(string):
        if 19 <= i <= 32 and "f" <= char <= "o":
            continue
        else:
            new_string += char
    return new_string
