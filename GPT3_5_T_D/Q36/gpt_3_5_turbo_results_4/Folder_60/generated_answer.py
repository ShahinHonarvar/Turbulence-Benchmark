
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if 23 <= i < 83:
            if 'f' < string[i] < 'o':
                continue
        filtered_string += string[i]
    return filtered_string
