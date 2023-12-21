
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i >= 55 and i < 66:
            if string[i] > 'f' and string[i] < '|':
                continue
        filtered_string += string[i]
    return filtered_string
