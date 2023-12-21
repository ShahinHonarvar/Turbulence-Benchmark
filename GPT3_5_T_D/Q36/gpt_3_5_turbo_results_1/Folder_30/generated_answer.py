
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if 23 <= i < 45 and '3' < string[i] < 'I':
            continue
        filtered_string += string[i]
    return filtered_string
