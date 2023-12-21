
def filter_chars(string):
    filtered_string = ""
    for char in string:
        if ord(char) >= 74 and ord(char) <= 81:
            continue
        else:
            filtered_string += char

    return filtered_string
