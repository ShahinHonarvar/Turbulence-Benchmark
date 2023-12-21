
def filter_chars(string):
    filtered_string = ""
    for char in string:
        if 42 <= ord(char) <= 97 and '*' <= char <= 'b':
            continue
        filtered_string += char
    return filtered_string
