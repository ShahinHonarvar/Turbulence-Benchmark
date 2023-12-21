
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i < 10 or i > 69 or string[i] < 'I' or string[i] > 'K':
            filtered_string += string[i]
    return filtered_string
