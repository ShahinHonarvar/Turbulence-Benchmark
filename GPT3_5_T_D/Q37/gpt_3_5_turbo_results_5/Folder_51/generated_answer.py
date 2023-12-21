
def filter_chars(string):
    filtered_string = ""
    for index, char in enumerate(string):
        if index < 36 or index > 40:
            filtered_string += char
        elif char < 'H' or char > 'e':
            filtered_string += char
    return filtered_string
