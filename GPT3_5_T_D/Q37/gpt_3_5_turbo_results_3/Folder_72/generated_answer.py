
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i >= 35 and i <= 51 and string[i] >= 'H' and string[i] <= 's':
            continue
        filtered_string += string[i]
    return filtered_string
