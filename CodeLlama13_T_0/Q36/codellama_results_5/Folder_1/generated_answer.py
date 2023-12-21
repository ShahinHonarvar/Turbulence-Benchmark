
def filter_chars(string):
    new_str = ""
    for i, char in enumerate(string):
        if i < 69 or i > 87:
            new_str += char
        elif char > "#" and char < "L":
            new_str += char
    return new_str
