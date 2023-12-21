
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if i >= 11 and i < 46 and char > "!" and char < "A":
            continue
        filtered_string += char
    return filtered_string
