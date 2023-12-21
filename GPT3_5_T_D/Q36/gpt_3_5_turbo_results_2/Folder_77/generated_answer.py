
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if 221 <= i < 419 and '-' < string[i] < 'v':
            continue
        filtered_string += string[i]
    return filtered_string
