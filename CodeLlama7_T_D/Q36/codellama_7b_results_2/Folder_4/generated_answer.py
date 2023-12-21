
def filter_chars(string):
    filtered_string = ""
    for i in range(42, 67):
        if string[i].isalpha() and (string[i] > '6' and string[i] < 'g'):
            filtered_string += string[i]
    return filtered_string
