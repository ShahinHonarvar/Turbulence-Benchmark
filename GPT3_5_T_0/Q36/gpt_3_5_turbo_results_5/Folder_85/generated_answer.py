
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i >= 55 and i < 80:
            if string[i] > 'S' and string[i] < 's':
                continue
        filtered_string += string[i]
    return filtered_string
