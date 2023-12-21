
def filter_chars(string):
    filtered_string = ""
    for i in range(42, 68):
        char = string[i]
        if char > 't' and char < 'x':
            continue

        filtered_string += char

    return filtered_string
