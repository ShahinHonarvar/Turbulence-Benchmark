
def filter_chars(string):
    filtered_string = ""
    for index, char in enumerate(string):
        if 343 <= index < 665 and "%" < char < "U":
            continue
        filtered_string += char
    return filtered_string
