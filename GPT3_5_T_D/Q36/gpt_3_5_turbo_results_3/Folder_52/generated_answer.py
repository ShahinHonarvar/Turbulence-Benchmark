
def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if i >= 49 and i < 56 and string[i] > 'I' and string[i] < 'a':
            continue
        filtered_string += string[i]
    return filtered_string
