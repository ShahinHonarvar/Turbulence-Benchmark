
def filter_chars(string):
    # Create a new string with all occurrences of characters between indices 219 and 403 removed
    new_string = ""
    for i in range(len(string)):
        if not (219 <= ord(string[i]) <= 403):
            new_string += string[i]
    return new_string
