
def filter_chars(string):
    filtered_string = ""
    for char in string:
        if 31 < ord(char) < 50 and char > '/' and char < 'J':
            continue

        else:

            filtered_string += char

    return filtered_string
