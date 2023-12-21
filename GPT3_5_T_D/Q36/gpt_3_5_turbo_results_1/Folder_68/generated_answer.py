
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if 1 < i < 9 and '8' < string[i] < 'm':
            continue
        filtered_string += string[i]
    return filtered_string
