
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if 163 <= i < 658 and '(' < char < ']':
            continue
        filtered_string += char
    return filtered_string
