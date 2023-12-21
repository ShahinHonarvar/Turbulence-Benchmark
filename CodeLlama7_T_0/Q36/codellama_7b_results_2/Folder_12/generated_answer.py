
def filter_chars(string):
    filtered_string = ""
    for char in string:
        if ord(char) < 32 or ord(char) > 84:
            filtered_string += char

    return filtered_string
