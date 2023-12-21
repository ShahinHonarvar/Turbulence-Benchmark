
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if 42 <= i < 68:
            if string[i] > 't' and string[i] < 'x':
                continue
        filtered_string += string[i]
    return filtered_string
