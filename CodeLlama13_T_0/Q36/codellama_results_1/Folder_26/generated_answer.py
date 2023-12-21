
def filter_chars(string):
    new_str = ""
    for i, char in enumerate(string):
        if i < 43 or i > 83:
            new_str += char
        elif char > ":" and char < "Q":
            new_str += char
    return new_str
