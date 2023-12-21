
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if 283 <= i < 484 and 'l' < string[i] < 't':
            continue
        filtered_string += string[i]
    return filtered_string
