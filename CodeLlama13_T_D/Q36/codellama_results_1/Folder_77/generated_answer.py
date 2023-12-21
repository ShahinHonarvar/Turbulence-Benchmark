
def filter_chars(string):
    filtered_string = ""
    for char in string:
        if 221 < ord(char) < 419 and char > "-" and char < "v":
            filtered_string += char
    return filtered_string
