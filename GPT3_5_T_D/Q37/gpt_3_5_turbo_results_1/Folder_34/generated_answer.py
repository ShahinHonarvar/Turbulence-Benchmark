
def filter_chars(string):
    filtered_string = ""
    for index, char in enumerate(string):
        if index >= 54 and index <= 62 and char >= ')' and char <= '9':
            continue
        filtered_string += char
    return filtered_string
