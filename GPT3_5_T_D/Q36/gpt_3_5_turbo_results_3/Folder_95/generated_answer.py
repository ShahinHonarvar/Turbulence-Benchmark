
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if 56 <= i < 86 and '+' < string[i] < 'w':
            continue
        filtered_string += string[i]
    return filtered_string
