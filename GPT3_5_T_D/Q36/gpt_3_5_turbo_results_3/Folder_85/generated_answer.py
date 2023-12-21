
def filter_chars(string):
    filtered_string = ''
    for i in range(55, 80):
        if 'S' < string[i] < 's':
            continue
        filtered_string += string[i]
    return string[:55] + filtered_string + string[80:]
