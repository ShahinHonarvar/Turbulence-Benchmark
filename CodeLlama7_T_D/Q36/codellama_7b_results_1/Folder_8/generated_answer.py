
def filter_chars(string):
    # Create a new string with the filtered characters
    filtered_string = ""

    for char in string:
        if not (82 < ord(char) < 93):
            filtered_string += char

    return filtered_string
