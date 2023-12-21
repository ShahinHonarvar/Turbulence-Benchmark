
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if 46 < i < 91:
            if "D" < char < "H":
                continue
        filtered_string += char
    return filtered_string
