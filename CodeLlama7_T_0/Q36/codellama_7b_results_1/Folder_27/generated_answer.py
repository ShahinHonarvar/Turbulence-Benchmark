
def filter_chars(string):
    filtered_string = ""
    for char in string:
        if ord(char) < 48 or ord(char) > 75:
            filtered_string += char

    return filtered_string
