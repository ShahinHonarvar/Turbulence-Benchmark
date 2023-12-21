
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i >= 56 and i < 86:
            if string[i] > '+' and string[i] < 'w':
                continue
        filtered_string += string[i]
    return filtered_string
