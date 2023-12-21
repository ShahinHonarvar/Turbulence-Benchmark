
def filter_chars(string):
    filtered_string = ""
    for index, char in enumerate(string):
        if index < 22 or index > 85:
            filtered_string += char
        elif char.isnumeric() or ('a' <= char <= 'e'):
            filtered_string += char
    return filtered_string
