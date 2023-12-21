
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i >= 154 and i < 222:
            if string[i] > 'A' and string[i] < 'f':
                continue
        filtered_string += string[i]
    return filtered_string
