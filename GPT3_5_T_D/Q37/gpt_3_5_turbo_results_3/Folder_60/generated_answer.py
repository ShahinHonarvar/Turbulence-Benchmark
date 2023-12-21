
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i >= 12 and i <= 77 and string[i] >= ':' and string[i] <= 'L':
            continue
        filtered_string += string[i]
    return filtered_string
