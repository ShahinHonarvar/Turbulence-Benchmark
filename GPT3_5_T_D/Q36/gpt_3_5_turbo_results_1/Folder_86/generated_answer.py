
def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if 672 <= i < 709:
            if 'X' < string[i] < '}':
                continue
        filtered_string += string[i]
    return filtered_string
