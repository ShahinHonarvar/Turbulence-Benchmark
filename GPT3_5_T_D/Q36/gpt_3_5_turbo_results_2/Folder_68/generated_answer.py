
def filter_chars(string):
    filtered_string = ""
    for char in string:
        if char > '8' and char < 'm':
            continue
        filtered_string += char
    return filtered_string
