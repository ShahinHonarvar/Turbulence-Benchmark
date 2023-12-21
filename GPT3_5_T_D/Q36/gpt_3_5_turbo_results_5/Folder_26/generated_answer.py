
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if 43 <= i < 83 and char > ":" and char < "Q":
            continue
        filtered_string += char
    return filtered_string
