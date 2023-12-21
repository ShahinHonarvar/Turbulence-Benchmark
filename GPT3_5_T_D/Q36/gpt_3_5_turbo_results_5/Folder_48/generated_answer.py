
def filter_chars(string):
    filtered_string = ""
    for index, char in enumerate(string):
        if index >= 154 and index < 222:
            if char > 'A' and char < 'f':
                continue
        filtered_string += char
    return filtered_string
