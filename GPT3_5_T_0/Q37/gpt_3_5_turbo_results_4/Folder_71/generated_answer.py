
def filter_chars(string):
    filtered_string = ""
    for char in string:
        if 32 <= ord(char) <= 46 and '0' <= char <= 'k':
            continue
        filtered_string += char
    return filtered_string
