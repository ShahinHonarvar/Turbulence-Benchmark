
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i >= 46 and i < 91:
            if 'D' < string[i] < 'H':
                continue
        filtered_string += string[i]
    return filtered_string
