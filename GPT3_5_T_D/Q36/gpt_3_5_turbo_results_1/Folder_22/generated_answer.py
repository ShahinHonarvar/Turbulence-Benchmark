
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if 55 <= i < 84:
            if string[i] > ';' and string[i] < 'z':
                continue
        filtered_string += string[i]
    return filtered_string
