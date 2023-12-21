
def filter_chars(string):
    filtered_string = ""
    for index, char in enumerate(string):
        if 69 <= index <= 80 and "@" <= char <= "p":
            continue
        filtered_string += char
    return filtered_string
