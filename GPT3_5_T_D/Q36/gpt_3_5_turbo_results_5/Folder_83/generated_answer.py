
def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if i < 72 or i >= 93 or string[i] <= '<' or string[i] >= 'J':
            filtered_string += string[i]
    return filtered_string
