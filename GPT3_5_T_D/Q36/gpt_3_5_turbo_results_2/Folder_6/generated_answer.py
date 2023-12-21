
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if 31 < i < 70 and 'B' < string[i] < 'v':
            continue
        filtered_string += string[i]
    return filtered_string
