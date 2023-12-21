
def filter_chars(string):
    new_str = ""
    for i, char in enumerate(string):
        if i < 58 or i > 81:
            new_str += char
        elif char > "5" and char < ">":
            new_str += char
    return new_str
