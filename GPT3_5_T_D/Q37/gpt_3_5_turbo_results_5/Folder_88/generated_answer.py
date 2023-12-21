
def filter_chars(string):
    filtered_string = ""
    for character in string:
        if 69 <= string.index(character) <= 80 and '@' <= character <= 'p':
            continue
        filtered_string += character
    return filtered_string
