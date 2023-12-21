
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i >= 35 and i < 60:
            if string[i] > '!' and string[i] < 'B':
                continue
        filtered_string += string[i]
    return filtered_string
