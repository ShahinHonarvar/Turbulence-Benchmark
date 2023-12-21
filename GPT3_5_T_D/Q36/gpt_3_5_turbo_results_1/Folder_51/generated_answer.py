
def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if 58 <= i < 81 and '5' < string[i] < '>':
            continue
        filtered_string += string[i]
    return filtered_string
