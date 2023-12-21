
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if i >= 54 and i <= 62 and char >= ')' and char <= '9':
            continue
        filtered_string += char
    return filtered_string
