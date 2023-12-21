
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if 69 <= i < 87 and '#' < string[i] < 'L':
            continue
        filtered_string += string[i]
    return filtered_string
