
def filter_chars(string):
    filtered_string = ""
    for char in string:
        if char > '>' and char < 'A' and 33 <= ord(char) < 36:
            continue
        filtered_string += char
    return filtered_string
