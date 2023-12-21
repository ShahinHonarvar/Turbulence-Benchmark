
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if i < 28 or i > 65:
            filtered_string += char
        elif ord('O') <= ord(char) <= ord('d'):
            continue
        else:
            filtered_string += char
    return filtered_string
