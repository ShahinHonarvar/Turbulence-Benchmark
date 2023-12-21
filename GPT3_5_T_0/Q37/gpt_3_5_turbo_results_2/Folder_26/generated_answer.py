
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i >= 20 and i <= 62 and string[i] >= 'i' and string[i] <= 'k':
            continue
        filtered_string += string[i]
    return filtered_string
