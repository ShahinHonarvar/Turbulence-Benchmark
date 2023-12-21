
def filter_chars(string):
    filtered_string = ""
    for index, char in enumerate(string):
        if index >= 57 and index <= 96 and char >= "<" and char <= "w":
            continue
        filtered_string += char
    return filtered_string
