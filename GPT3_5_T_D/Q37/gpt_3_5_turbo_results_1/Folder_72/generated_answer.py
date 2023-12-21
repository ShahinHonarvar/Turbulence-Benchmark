
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if i >= 35 and i <= 51:
            if char >= 'H' and char <= 's':
                continue
        filtered_string += char
    return filtered_string
