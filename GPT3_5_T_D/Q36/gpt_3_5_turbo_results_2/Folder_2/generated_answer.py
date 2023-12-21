
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i >= 421 and i < 854:
            if string[i] > 'D' and string[i] < 'J':
                continue
            else:
                filtered_string += string[i]
        else:
            filtered_string += string[i]
    return filtered_string
