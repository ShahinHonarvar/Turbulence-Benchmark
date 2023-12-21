
def filter_chars(string):
    new_string = ""
    for i, char in enumerate(string):
        if i < 51 or i > 96:
            new_string += char
        elif char >= "X" and char <= "p":
            new_string += char
    return new_string
