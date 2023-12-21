
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i < 43 or i >= 83:
            filtered_string += string[i]
        elif string[i] > ':' and string[i] < 'Q':
            filtered_string = filtered_string.replace(string[i], '')
    return filtered_string
