
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if i >= 75 and i <= 99 and char >= '8' and char <= 'e':
            continue
        filtered_string += char
    return filtered_string
