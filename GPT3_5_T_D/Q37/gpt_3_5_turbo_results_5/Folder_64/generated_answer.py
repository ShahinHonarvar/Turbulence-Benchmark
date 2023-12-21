
def filter_chars(string):
    filtered_string = ""
    for index, char in enumerate(string):
        if index >= 1 and index <= 7 and char >= 'L' and char <= 'a':
            continue
        filtered_string += char
    return filtered_string
