
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if 72 <= i <= 94 and '.' <= string[i] <= 'b':
            continue
        filtered_string += string[i]
    return filtered_string
