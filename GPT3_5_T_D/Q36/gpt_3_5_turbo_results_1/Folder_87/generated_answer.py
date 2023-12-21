
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if i < 32 or i >= 61:
            filtered_string += char
        elif char > '3' and char < 'D':
            continue
        else:
            filtered_string += char
    return filtered_string
