
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if i >= 23 and i <= 89 and char >= 'w' and char <= '{':
            continue
        filtered_string += char
    return filtered_string
