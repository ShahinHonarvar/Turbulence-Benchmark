
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if i >= 24 and i <= 82 and char >= '5' and char <= '<':
            continue
        filtered_string += char
    return filtered_string
