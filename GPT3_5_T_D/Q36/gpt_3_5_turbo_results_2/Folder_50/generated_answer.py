
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if 61 < i < 88 and "%" < char < "q":
            continue
        filtered_string += char
    return filtered_string
