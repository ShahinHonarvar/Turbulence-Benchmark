
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if 17 <= i <= 63 and "O" <= char <= "^":
            continue
        filtered_string += char
    return filtered_string
