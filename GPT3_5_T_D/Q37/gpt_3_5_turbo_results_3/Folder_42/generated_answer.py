
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i >= 73 and i <= 74:
            if string[i] >= 'U' and string[i] <= 'l':
                continue
        filtered_string += string[i]
    return filtered_string
