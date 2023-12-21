
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i >= 21 and i < 25:
            if string[i] > '5' and string[i] < '}':
                continue
        filtered_string += string[i]
    return filtered_string
