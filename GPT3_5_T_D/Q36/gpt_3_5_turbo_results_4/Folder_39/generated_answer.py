
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if 43 <= i < 59 and '5' < char < 'C':
            continue
        filtered_string += char
    return filtered_string
