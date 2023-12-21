
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if 14 <= i < 75 and '9' < string[i] < 'K':
            continue
        filtered_string += string[i]
    return filtered_string
