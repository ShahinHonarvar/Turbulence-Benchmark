
def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if i >= 11 and i <= 32 and string[i] >= '!' and string[i] <= '@':
            continue
        filtered_string += string[i]
    return filtered_string
